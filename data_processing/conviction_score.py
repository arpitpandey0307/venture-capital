# data_processing/conviction_score.py

import os
import sys
import certifi
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

# Ensure sibling modules (metrics, sentiment) are importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from metrics import fetch_raw_projects, process_all_metrics
from sentiment import run_sentiment_pipeline

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"), tlsCAFile=certifi.where())
db = client["venture_alpha"]
collection = db["signals"]

# ── Weights (must sum to 1.0) ──────────────────
W_STAR_VELOCITY          = 0.40
W_CONTRIBUTOR_DIVERSITY  = 0.30
W_SOCIAL_SENTIMENT       = 0.20
W_NEWS_MENTIONS          = 0.10
INVESTMENT_LEAD_THRESHOLD = 0.85

SOURCE_WEIGHTS = {
    "github":      1.0,   # most reliable — real code activity
    "hackernews":  0.8,   # developer discussion, high signal
    "exa":         0.6,   # news/articles, useful but noisier
}


def apply_source_weight(score: float, source: str) -> float:
    """
    Multiply the raw conviction score by a source trust factor.
    GitHub signals are taken at full value; Exa signals are slightly discounted.
    """
    weight = SOURCE_WEIGHTS.get(source, 0.7)
    return round(score * weight, 4)


def get_news_mentions_score(tags) -> float:
    """
    Member 1 provides a 'tags' array on every document.
    We use the number of relevant VC/tech tags as a proxy
    for news coverage until a dedicated news_mentions collection exists.

    High-signal tags get a boost.
    Score is normalized to 0.0 - 1.0, capped at 1.0.
    """
    if not tags or not isinstance(tags, list):
        return 0.3   # low default

    high_signal_tags = {
        "AI", "agents", "LLM", "vector-database", "YCombinator",
        "open-source", "autonomous", "infrastructure", "startup"
    }

    # Count how many of this doc's tags are high-signal
    matches = sum(1 for tag in tags if tag in high_signal_tags)
    return round(min(matches / 3.0, 1.0), 4)   # 3 matches = full score


def calculate_conviction_score(sv_norm, diversity, sentiment, news) -> float:
    """
    CS = 0.4×star_velocity_norm + 0.3×diversity + 0.2×sentiment + 0.1×news
    All inputs and output: 0.0 to 1.0
    """
    score = (
        W_STAR_VELOCITY         * float(sv_norm)
        + W_CONTRIBUTOR_DIVERSITY * float(diversity)
        + W_SOCIAL_SENTIMENT      * float(sentiment)
        + W_NEWS_MENTIONS         * float(news)
    )
    return round(score, 4)


def save_scores_to_mongo(df: pd.DataFrame):
    """
    Write scores back into MongoDB.
    Member 1 uses 'url' as the unique primary key, so we match on that.
    update_one with upsert=False — we only update existing docs, never insert new ones.
    """
    updated = 0
    skipped = 0
    for _, row in df.iterrows():
        url = row.get("url")
        if not url:
            skipped += 1
            continue

        collection.update_one(
            {"url": url},
            {"$set": {
                "conviction_score":       float(row["conviction_score"]),
                "is_investment_lead":     bool(row["is_investment_lead"]),
                "social_sentiment":       float(row["social_sentiment"]),
                "star_velocity":          float(row["star_velocity"]),
                "contributor_diversity":  float(row["contributor_diversity"]),
                "star_velocity_norm":     float(row["star_velocity_norm"]),
            }},
            upsert=False
        )
        updated += 1

    print(f"[conviction_score.py] Updated {updated} documents in MongoDB.")
    if skipped:
        print(f"[conviction_score.py] Skipped {skipped} documents (no 'url' field).")


def run_full_pipeline():
    print("=" * 55)
    print("Member 2 pipeline starting...")
    print("=" * 55)

    # 1. Fetch
    df = fetch_raw_projects()
    if df.empty:
        print("No signals found in MongoDB. Check MONGO_URI and collection name.")
        return

    print(f"Fetched {len(df)} signals from MongoDB Atlas.")

    # 2. Metrics
    df = process_all_metrics(df)

    # 3. Sentiment
    df = run_sentiment_pipeline(df)

    # 4. Conviction scores
    scores, flags = [], []
    for _, row in df.iterrows():
        news = get_news_mentions_score(row.get("tags", []))
        cs = apply_source_weight(
            calculate_conviction_score(
                row["star_velocity_norm"],
                row["contributor_diversity"],
                row["social_sentiment"],
                news
            ),
            row.get("source", "exa")
        )
        scores.append(cs)
        flags.append(cs >= INVESTMENT_LEAD_THRESHOLD)

    df["conviction_score"]    = scores
    df["is_investment_lead"]  = flags

    # 5. Print ranked results
    print("\n" + "=" * 55)
    print("CONVICTION SCORE RESULTS (top 10)")
    print("=" * 55)

    display_cols = ["repo_name", "source", "star_velocity",
                    "social_sentiment", "conviction_score", "is_investment_lead"]
    # Only use columns that actually exist
    display_cols = [c for c in display_cols if c in df.columns]

    top = df[display_cols] \
            .sort_values("conviction_score", ascending=False) \
            .head(10)
    print(top.to_string(index=False))

    leads = df[df["is_investment_lead"]]
    print(f"\n>>> {len(leads)} INVESTMENT LEADS (score >= {INVESTMENT_LEAD_THRESHOLD})")
    for _, lead in leads.iterrows():
        src = lead.get("source", "unknown")
        name = lead.get("repo_name", "unnamed")
        print(f"    [{str(src).upper()}] {name} — {lead['conviction_score']}")

    # 6. Save back to MongoDB
    try:
        save_scores_to_mongo(df)
    except Exception as e:
        print(f"\n[WARNING] Could not save scores to MongoDB: {e}")
        print("Your DB user may only have read permissions. Update role to 'Read and Write' in Atlas → Database Access.")
    print("\nMember 2 pipeline complete.")
    return df


if __name__ == "__main__":
    run_full_pipeline()
