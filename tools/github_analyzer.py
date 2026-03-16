"""
tools/github_analyzer.py
------------------------
Tool 1 — Repository Technology Analyzer

Uses Gemini 2.0 Flash (google.genai SDK) to analyse a repository's technology.
"""

import json
import logging
from typing import Dict, Any

from google import genai

from config import settings
from models.schemas import TechAnalysisOutput
from utils.prompt_templates import technology_analysis_prompt

logger = logging.getLogger(__name__)

# Initialise the new google.genai client
_client = genai.Client(api_key=settings.GEMINI_API_KEY)


def _call_gemini(prompt: str) -> str:
    """
    Call Gemini via the new google.genai SDK and return the raw text response.

    Args:
        prompt: The prompt string to send.

    Returns:
        Raw text from Gemini, with markdown fences stripped.
    """
    response = _client.models.generate_content(
        model=settings.GEMINI_MODEL,
        contents=prompt
    )
    raw = response.text.strip()

    # Strip markdown code fences if Gemini wraps output in ```json ... ```
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    return raw


def analyze_repository(repo_data: Dict[str, Any]) -> TechAnalysisOutput:
    """
    Analyse a repository using Gemini and return structured technology insights.

    Args:
        repo_data: Dictionary matching the RepoInput schema fields.

    Returns:
        TechAnalysisOutput with technology_summary, key_use_cases,
        and industry_impact.
    """
    logger.info(f"Analysing repository: {repo_data.get('repo_name')}")

    prompt = technology_analysis_prompt(repo_data)
    raw_text = _call_gemini(prompt)

    try:
        data = json.loads(raw_text)
    except json.JSONDecodeError:
        logger.error(f"Failed to parse Gemini response as JSON: {raw_text[:200]}")
        data = {
            "technology_summary": raw_text,
            "key_use_cases": "See technology_summary for details.",
            "industry_impact": "Unable to parse structured response."
        }

    return TechAnalysisOutput(
        technology_summary=data.get("technology_summary", ""),
        key_use_cases=data.get("key_use_cases", ""),
        industry_impact=data.get("industry_impact", "")
    )
