"""
services/analysis_service.py
------------------------------
Orchestration Service — Full AI Pipeline (Phase 2 Enhanced)

Now includes:
  • evidence_sources collection (repo_url + Exa article URLs)
  • analysis_time measurement
  • signal_breakdown passthrough
  • risks passthrough
  • compare_projects function
"""

import time
import logging
from typing import Dict, Any

from config import settings

from tools.github_analyzer import analyze_repository
from tools.research_tool import research_technology
from tools.founder_simulator import simulate_founder_interview
from agents.trend_agent import validate_trend
from agents.memo_agent import (
    generate_investment_memo,
    compute_conviction_score,
    compute_signal_breakdown
)
from models.schemas import FullAnalysisOutput, CompareProjectsOutput

logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────────────────────────────────────
# FULL PIPELINE RUNNER (Phase 2 enhanced)
# ─────────────────────────────────────────────────────────────────────────────

def run_full_pipeline(repo_data: Dict[str, Any]) -> FullAnalysisOutput:
    """
    Execute the complete 5-step AI pipeline with Phase 2 enhancements:
      • Collects evidence_sources (repo_url + Exa article URLs)
      • Measures total analysis_time
      • Includes signal_breakdown and risks

    Args:
        repo_data: Dict matching RepoInput fields.

    Returns:
        FullAnalysisOutput with all Phase 2 fields populated.
    """
    start_time = time.time()
    repo_name = repo_data.get("repo_name", "Unknown")
    logger.info(f"Starting full pipeline for: {repo_name}")

    # ── Evidence collection starts with the repo URL ─────────────────────────
    evidence_sources = []
    repo_url = repo_data.get("repo_url", "")
    if repo_url:
        evidence_sources.append(repo_url)

    # ── Step 1: Technology Analysis ───────────────────────────────────────────
    tech = analyze_repository(repo_data)
    logger.info("Step 1 complete: technology analysis")

    # ── Step 2: Web Research ──────────────────────────────────────────────────
    research = research_technology(repo_name)
    logger.info("Step 2 complete: web research")

    # Collect Exa article URLs as evidence
    evidence_sources.extend(research.sources)

    # ── Step 3: Trend Validation ──────────────────────────────────────────────
    trend = validate_trend(repo_data)
    logger.info("Step 3 complete: trend validation")

    # ── Step 4: Founder Interview ─────────────────────────────────────────────
    enriched_analysis = {
        **repo_data,
        "technology_summary": tech.technology_summary,
        "key_use_cases":      tech.key_use_cases,
        "industry_impact":    tech.industry_impact
    }
    interview = simulate_founder_interview(enriched_analysis)
    logger.info("Step 4 complete: founder interview simulation")

    # ── Step 5: Investment Memo ───────────────────────────────────────────────
    memo_input = {
        **repo_data,
        "technology_summary": tech.technology_summary,
        "key_use_cases":      tech.key_use_cases,
        "industry_impact":    tech.industry_impact,
        "research_summary":   research.research_summary,
        "trend_strength":     trend.trend_strength
    }
    memo = generate_investment_memo(memo_input)
    logger.info("Step 5 complete: investment memo generated")

    # ── Timing ────────────────────────────────────────────────────────────────
    elapsed = round(time.time() - start_time, 1)
    analysis_time = f"{elapsed} seconds"
    logger.info(f"Full pipeline completed in {analysis_time}")

    # De-duplicate evidence sources while preserving order
    seen = set()
    unique_evidence = []
    for url in evidence_sources:
        if url and url not in seen:
            seen.add(url)
            unique_evidence.append(url)

    return FullAnalysisOutput(
        # Tech analysis
        technology_summary=tech.technology_summary,
        key_use_cases=tech.key_use_cases,
        industry_impact=tech.industry_impact,
        # Research
        research_summary=research.research_summary,
        sources=research.sources,
        # Trend
        trend_strength=trend.trend_strength,
        trend_reasoning=trend.reasoning,
        # Interview
        founder_interview=interview,
        # Memo + conviction
        investment_memo=memo.memo,
        conviction_score=memo.conviction_score,
        # ── Phase 2 fields ──
        signal_breakdown=memo.signal_breakdown,
        risks=memo.risks,
        evidence_sources=unique_evidence,
        analysis_time=analysis_time
    )


# ─────────────────────────────────────────────────────────────────────────────
# COMPARE PROJECTS (Phase 2)
# ─────────────────────────────────────────────────────────────────────────────

def compare_projects(
    repo1_data: Dict[str, Any],
    repo2_data: Dict[str, Any]
) -> CompareProjectsOutput:
    """
    Compare two projects side-by-side on signal breakdown, conviction scores,
    and generate an AI-powered comparative analysis.

    Args:
        repo1_data: Dict for first repository.
        repo2_data: Dict for second repository.

    Returns:
        CompareProjectsOutput with scores, breakdowns, and recommendation.
    """
    start_time = time.time()

    name1 = repo1_data.get("repo_name", "Project 1")
    name2 = repo2_data.get("repo_name", "Project 2")
    logger.info(f"Comparing projects: {name1} vs {name2}")

    # Compute individual signals
    sb1 = compute_signal_breakdown(repo1_data)
    sb2 = compute_signal_breakdown(repo2_data)
    cs1 = compute_conviction_score(repo1_data)
    cs2 = compute_conviction_score(repo2_data)

    # Use Gemini for a qualitative comparison
    from google import genai
    client = genai.Client(api_key=settings.GEMINI_API_KEY)

    prompt = f"""
You are a senior VC investment analyst comparing two open-source projects.

Project 1: {name1}
  - Description: {repo1_data.get('description', '')}
  - Stars: {repo1_data.get('stars', 0):,} | Velocity: {repo1_data.get('star_velocity', 0)} stars/day
  - Contributors: {repo1_data.get('contributors', 0)}
  - Sentiment: {repo1_data.get('social_sentiment', 'neutral')}
  - News Mentions: {repo1_data.get('news_mentions', 0)}
  - Conviction Score: {cs1:.2f}

Project 2: {name2}
  - Description: {repo2_data.get('description', '')}
  - Stars: {repo2_data.get('stars', 0):,} | Velocity: {repo2_data.get('star_velocity', 0)} stars/day
  - Contributors: {repo2_data.get('contributors', 0)}
  - Sentiment: {repo2_data.get('social_sentiment', 'neutral')}
  - News Mentions: {repo2_data.get('news_mentions', 0)}
  - Conviction Score: {cs2:.2f}

Write TWO sections:

COMPARISON: A 3-4 sentence comparative analysis covering technology potential,
community momentum, and market timing.

RECOMMENDATION: One clear sentence stating which project is the stronger
investment bet and the single most important reason why.

Respond in EXACTLY this JSON format (no markdown fences, pure JSON):
{{
  "comparison_summary": "<comparison text>",
  "recommendation": "<recommendation text>"
}}
""".strip()

    try:
        response = client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=prompt
        )
        raw = response.text.strip()
        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
            raw = raw.strip()

        import json
        data = json.loads(raw)
        comparison_summary = data.get("comparison_summary", "")
        recommendation = data.get("recommendation", "")
    except Exception as e:
        logger.warning(f"Comparison Gemini call failed: {e}")
        winner = name1 if cs1 >= cs2 else name2
        comparison_summary = (
            f"{name1} scores {cs1:.2f} vs {name2} at {cs2:.2f}. "
            f"Based on quantitative signals, {winner} shows stronger momentum."
        )
        recommendation = f"{winner} is the stronger investment based on overall signal strength."

    elapsed = round(time.time() - start_time, 1)

    return CompareProjectsOutput(
        project1_name=name1,
        project2_name=name2,
        project1_score=cs1,
        project2_score=cs2,
        project1_breakdown=sb1,
        project2_breakdown=sb2,
        comparison_summary=comparison_summary,
        recommendation=recommendation,
        analysis_time=f"{elapsed} seconds"
    )


# ─────────────────────────────────────────────────────────────────────────────
# LANGCHAIN AGENT RUNNER (lazy imports — bonus feature)
# ─────────────────────────────────────────────────────────────────────────────

def run_langchain_agent(repo_data: Dict[str, Any]) -> str:
    """
    Run a LangChain agent over the pipeline tools (lazy-loaded).
    Falls back to sequential pipeline on any import failure.
    """
    logger.info(f"Running LangChain agent for: {repo_data.get('repo_name')}")

    try:
        from langchain_core.tools import Tool
        from langchain_google_genai import ChatGoogleGenerativeAI

        try:
            from langgraph.prebuilt import create_react_agent as _create_agent
            _use_langgraph = True
        except ImportError:
            _use_langgraph = False

        def _repo_tool(_: str) -> str:
            r = analyze_repository(repo_data)
            return f"Summary: {r.technology_summary}\nUses: {r.key_use_cases}\nImpact: {r.industry_impact}"

        def _research_tool(_: str) -> str:
            r = research_technology(repo_data.get("repo_name", ""))
            return f"Research: {r.research_summary}\nSources: {', '.join(r.sources[:3])}"

        def _trend_tool(_: str) -> str:
            r = validate_trend(repo_data)
            return f"Trend: {r.trend_strength}\nReasoning: {r.reasoning}"

        def _score_tool(_: str) -> str:
            return f"Conviction Score: {compute_conviction_score(repo_data):.2f}"

        tools = [
            Tool(name="repository_analyzer", func=_repo_tool,
                 description="Analyses a repository's technology and impact."),
            Tool(name="web_research", func=_research_tool,
                 description="Searches the web for articles about the technology."),
            Tool(name="trend_validator", func=_trend_tool,
                 description="Determines trend strength from project signals."),
            Tool(name="score_calculator", func=_score_tool,
                 description="Computes conviction score on a 0–1 scale."),
        ]

        llm = ChatGoogleGenerativeAI(
            model=settings.GEMINI_MODEL,
            google_api_key=settings.GEMINI_API_KEY,
            temperature=0.3,
            convert_system_message_to_human=True
        )

        query = (
            f"Analyse '{repo_data.get('repo_name')}': use all tools in sequence, "
            f"then summarise your investment thesis."
        )

        if _use_langgraph:
            agent = _create_agent(llm, tools)
            result = agent.invoke({"messages": [("user", query)]})
            msgs = result.get("messages", [])
            return msgs[-1].content if msgs else "Agent completed."
        else:
            return "LangChain agent unavailable. Use /full_analysis instead."

    except Exception as e:
        logger.warning(f"LangChain agent failed: {e}")
        full = run_full_pipeline(repo_data)
        return f"Technology: {full.technology_summary}\nTrend: {full.trend_strength}\nScore: {full.conviction_score}"
