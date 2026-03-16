"""
tools/founder_simulator.py
---------------------------
Tool 3 — Founder Interview Simulator

Two-stage pipeline:
  Pass 1 → Gemini generates 5 probing investor questions
  Pass 2 → Gemini simulates founder responses using repo context

Uses the new google.genai SDK.
"""

import json
import logging
from typing import Dict, Any, List

from google import genai

from config import settings
from models.schemas import InterviewOutput
from utils.prompt_templates import (
    founder_interview_questions_prompt,
    founder_interview_answers_prompt
)

logger = logging.getLogger(__name__)

# Initialise the new google.genai client
_client = genai.Client(api_key=settings.GEMINI_API_KEY)


def _call_gemini(prompt: str) -> str:
    """Call Gemini and return raw text response."""
    response = _client.models.generate_content(
        model=settings.GEMINI_MODEL,
        contents=prompt
    )
    return response.text.strip()


def _parse_json_list(raw: str, key: str) -> List[str]:
    """
    Safely parse a JSON object and extract a list under `key`.
    Handles markdown-fenced responses from Gemini.
    """
    text = raw.strip()
    if text.startswith("```"):
        parts = text.split("```")
        text = parts[1]
        if text.startswith("json"):
            text = text[4:]
        text = text.strip()

    try:
        data = json.loads(text)
        return data.get(key, [])
    except json.JSONDecodeError:
        logger.error(f"Failed to parse JSON for key '{key}': {text[:200]}")
        lines = [line.strip(" -•\t") for line in text.splitlines() if line.strip()]
        return lines[:5]


def simulate_founder_interview(repo_analysis: Dict[str, Any]) -> InterviewOutput:
    """
    Simulate a founder interview for a given project.

    Args:
        repo_analysis: Dict containing repo_name, technology_summary,
                       key_use_cases, industry_impact.

    Returns:
        InterviewOutput with matched questions and answers lists.
    """
    repo_name = repo_analysis.get("repo_name", "Unknown Project")
    logger.info(f"Simulating founder interview for: {repo_name}")

    # ── Pass 1: Generate Questions ────────────────────────────────────────────
    q_raw = _call_gemini(founder_interview_questions_prompt(repo_analysis))
    questions = _parse_json_list(q_raw, "questions")

    if not questions:
        questions = [
            f"What core problem does {repo_name} solve that existing tools cannot?",
            "What is your primary competitive moat?",
            "How do you plan to monetise this open-source project?",
            "Who is your target enterprise customer and what is your GTM strategy?",
            "Where do you see this project in three to five years?"
        ]

    # ── Pass 2: Simulate Founder Answers ─────────────────────────────────────
    a_raw = _call_gemini(founder_interview_answers_prompt(repo_analysis, questions))
    answers = _parse_json_list(a_raw, "answers")

    # Align both lists to the same length
    max_len = max(len(questions), len(answers))
    questions = (questions + [""] * max_len)[:max_len]
    answers = (answers + ["[No answer generated]"] * max_len)[:max_len]

    return InterviewOutput(questions=questions, answers=answers)
