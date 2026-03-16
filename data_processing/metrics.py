# data_processing/metrics.py

import os
import certifi
import pandas as pd
from datetime import datetime, timezone
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# Connect to MongoDB Atlas (certifi fixes TLS CA issues on Windows)
client = MongoClient(os.getenv("MONGO_URI"), tlsCAFile=certifi.where())
db = client["venture_alpha"]
collection = db["signals"]


def fetch_raw_projects() -> pd.DataFrame:
    """
    Pull all documents from the signals collection.
    MongoDB returns dicts — we convert straight to DataFrame.

    Member 1's schema fields we care about:
      source, repo_name, description, stars,
      contributors, created_utc, tags, url
    """
    docs = list(collection.find({}))
    df = pd.DataFrame(docs)

    # MongoDB _id is not JSON-serializable, drop it
    if "_id" in df.columns:
        df = df.drop(columns=["_id"])

    return df


def calculate_star_velocity(stars, created_utc) -> float:
    """
    star_velocity = stars / age_in_days

    created_utc is a Unix timestamp (integer) from Member 1's schema.
    Convert it to datetime first.
    """
    try:
        stars = int(stars) if stars else 0
        created_dt = datetime.fromtimestamp(int(created_utc), tz=timezone.utc)
        today = datetime.now(timezone.utc)
        age_days = (today - created_dt).days
        if age_days <= 0:
            age_days = 1
        return round(stars / age_days, 4)
    except Exception:
        return 0.0


def calculate_contributor_diversity(contributors, stars) -> float:
    """
    For non-GitHub sources (HackerNews, Exa), contributors = 0.
    In those cases we use stars (upvotes) as a proxy denominator.

    contributor_diversity = contributors / max(stars, 1)
    Capped at 1.0.
    """
    try:
        contributors = int(contributors) if contributors else 0
        stars = int(stars) if stars else 1
        if stars == 0:
            stars = 1
        diversity = contributors / stars
        return round(min(diversity, 1.0), 4)
    except Exception:
        return 0.0


def calculate_repo_age_days(created_utc) -> int:
    try:
        created_dt = datetime.fromtimestamp(int(created_utc), tz=timezone.utc)
        return (datetime.now(timezone.utc) - created_dt).days
    except Exception:
        return 0


def normalize(value: float, min_val: float, max_val: float) -> float:
    if max_val == min_val:
        return 0.0
    return round((value - min_val) / (max_val - min_val), 4)


def process_all_metrics(df: pd.DataFrame) -> pd.DataFrame:
    df["star_velocity"] = df.apply(
        lambda row: calculate_star_velocity(row.get("stars", 0), row.get("created_utc", 0)),
        axis=1
    )

    df["contributor_diversity"] = df.apply(
        lambda row: calculate_contributor_diversity(
            row.get("contributors", 0), row.get("stars", 1)
        ),
        axis=1
    )

    if "created_utc" in df.columns:
        df["repo_age_days"] = df["created_utc"].apply(calculate_repo_age_days)
    else:
        df["repo_age_days"] = 0

    # Normalize star_velocity to 0-1 across the whole dataset
    min_vel = df["star_velocity"].min()
    max_vel = df["star_velocity"].max()
    df["star_velocity_norm"] = df["star_velocity"].apply(
        lambda v: normalize(v, min_vel, max_vel)
    )

    print(f"[metrics.py] Processed {len(df)} signals.")
    return df


if __name__ == "__main__":
    df = fetch_raw_projects()
    df = process_all_metrics(df)
    if not df.empty:
        print(df[["repo_name", "source", "star_velocity", "contributor_diversity"]].head(10))
