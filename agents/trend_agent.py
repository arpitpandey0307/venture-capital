"""
agents/trend_agent.py
----------------------
Agent — Trend Validation

Uses Gemini 2.0 Flash (google.genai SDK) to assess trend strength.
"""

import json
import logging
from typing import Dict, Any

from google import genai

from config import settings
from models.schemas import TrendOutput
from utils.prompt_templates import trend_validation_prompt

logger = logging.getLogger(__name__)

# Initialise the new google.genai client
_client = genai.Client(api_key=settings.GEMINI_API_KEY)


def validate_trend(metrics: Dict[str, Any]) -> TrendOutput:
    """
    Evaluate project signals and determine trend strength.

    Args:
        metrics: Dict with star_velocity, contributors, social_sentiment,
                 news_mentions.

    Returns:
        TrendOutput with trend_strength (Low/Medium/High) and reasoning.
    """
    logger.info(
        f"Validating trend — velocity={metrics.get('star_velocity')}, "
        f"sentiment={metrics.get('social_sentiment')}"
    )

    prompt = trend_validation_prompt(metrics)
    response = _client.models.generate_content(
        model=settings.GEMINI_MODEL,
        contents=prompt
    )
    raw_text = response.text.strip()

    # Strip markdown fences if present
    if raw_text.startswith("```"):
        raw_text = raw_text.split("```")[1]
        if raw_text.startswith("json"):
            raw_text = raw_text[4:]
        raw_text = raw_text.strip()

    try:
        data = json.loads(raw_text)
        trend_strength = data.get("trend_strength", "Medium")
        reasoning = data.get("reasoning", raw_text)
    except json.JSONDecodeError:
        logger.warning("Could not parse Gemini trend response as JSON. Using heuristic fallback.")
        sv = float(metrics.get("star_velocity", 0))
        sentiment = str(metrics.get("social_sentiment", "neutral")).lower()
        mentions = int(metrics.get("news_mentions", 0))

        if sv > 30 and sentiment == "positive" and mentions >= 10:
            trend_strength = "High"
        elif sv > 10 or (sentiment == "positive" and mentions >= 5):
            trend_strength = "Medium"
        else:
            trend_strength = "Low"

        reasoning = raw_text if raw_text else (
            f"Heuristic assessment: velocity={sv}, sentiment={sentiment}, mentions={mentions}"
        )

    # Normalise capitalisation
    if trend_strength not in {"High", "Medium", "Low"}:
        trend_strength = "Medium"

    return TrendOutput(trend_strength=trend_strength, reasoning=reasoning)
