"""
utils/prompt_templates.py
--------------------------
Reusable, parameterised prompt strings for all Gemini calls.

Design principles:
  • Each builder function accepts typed arguments and returns a plain str.
  • Prompts are explicit and structured so Gemini returns predictable outputs.
  • All prompts instruct the model to stay factual and concise (hackathon-safe).
"""

from typing import Dict, Any


# ─────────────────────────────────────────────────────────────────────────────
# 1. TECHNOLOGY ANALYSIS PROMPT
# ─────────────────────────────────────────────────────────────────────────────

def technology_analysis_prompt(repo_data: Dict[str, Any]) -> str:
    """
    Builds a prompt asking Gemini to analyse a repository's technology.

    Args:
        repo_data: dict with keys repo_name, description, stars, contributors.

    Returns:
        Formatted prompt string.
    """
    return f"""
You are a senior technology analyst at a top venture capital firm.

Analyse the following open-source repository and provide a structured assessment.

Repository Details:
  - Name        : {repo_data.get('repo_name', 'Unknown')}
  - Description : {repo_data.get('description', 'N/A')}
  - GitHub Stars: {repo_data.get('stars', 0):,}
  - Contributors: {repo_data.get('contributors', 0)}
  - Star Velocity (stars/day): {repo_data.get('star_velocity', 0)}

Respond in EXACTLY this JSON format (no markdown fences, pure JSON):
{{
  "technology_summary": "<2-3 sentence explanation of what this technology does and how it works>",
  "key_use_cases": "<comma-separated list of 3-5 primary developer use-cases>",
  "industry_impact": "<which industries this technology disrupts or enables and why>"
}}
""".strip()


# ─────────────────────────────────────────────────────────────────────────────
# 2. TREND VALIDATION PROMPT
# ─────────────────────────────────────────────────────────────────────────────

def trend_validation_prompt(metrics: Dict[str, Any]) -> str:
    """
    Builds a prompt asking Gemini to evaluate whether a project represents
    an emerging tech trend.

    Args:
        metrics: dict with star_velocity, contributors, social_sentiment,
                 news_mentions.

    Returns:
        Formatted prompt string.
    """
    return f"""
You are a venture capital trend analyst specialising in emerging technologies.

Evaluate the following project signals and determine the strength of the
technology trend this project represents.

Signals:
  - Star Velocity (stars added per day) : {metrics.get('star_velocity', 0)}
  - Number of Contributors              : {metrics.get('contributors', 0)}
  - Social Sentiment                    : {metrics.get('social_sentiment', 'neutral')}
  - News / Blog Mentions (recent)       : {metrics.get('news_mentions', 0)}

Trend Strength Criteria:
  High   → Rapidly growing community, positive sentiment, multiple news mentions
  Medium → Moderate growth, mixed signals, some traction
  Low    → Slow growth, limited community, little external validation

Respond in EXACTLY this JSON format (no markdown fences, pure JSON):
{{
  "trend_strength": "<High|Medium|Low>",
  "reasoning": "<3-4 sentences explaining your assessment based on the signals above>"
}}
""".strip()


# ─────────────────────────────────────────────────────────────────────────────
# 3. FOUNDER INTERVIEW PROMPT
# ─────────────────────────────────────────────────────────────────────────────

def founder_interview_questions_prompt(repo_analysis: Dict[str, Any]) -> str:
    """
    Prompt: generate VC due-diligence questions for this project.

    Args:
        repo_analysis: dict with technology_summary, key_use_cases,
                       industry_impact, repo_name.

    Returns:
        Formatted prompt string.
    """
    return f"""
You are a Partner at a top-tier venture capital firm conducting a first-meeting
due diligence call with the founders of the following project:

Project: {repo_analysis.get('repo_name', 'Unknown')}
Technology Summary: {repo_analysis.get('technology_summary', '')}
Key Use Cases: {repo_analysis.get('key_use_cases', '')}
Industry Impact: {repo_analysis.get('industry_impact', '')}

Generate exactly 5 sharp, probing VC due-diligence questions covering:
  1. The core problem being solved
  2. Competitive advantage / moat
  3. Monetisation model
  4. Target market and customer segment
  5. Long-term vision (3-5 year)

Respond in EXACTLY this JSON format (no markdown fences, pure JSON):
{{
  "questions": [
    "<question 1>",
    "<question 2>",
    "<question 3>",
    "<question 4>",
    "<question 5>"
  ]
}}
""".strip()


def founder_interview_answers_prompt(
    repo_analysis: Dict[str, Any],
    questions: list
) -> str:
    """
    Prompt: simulate founder answers to the given VC questions.

    Args:
        repo_analysis: same dict used for questions.
        questions: list of question strings.

    Returns:
        Formatted prompt string.
    """
    questions_text = "\n".join(
        f"  Q{i+1}: {q}" for i, q in enumerate(questions)
    )
    return f"""
You are the founder of {repo_analysis.get('repo_name', 'this project')}.

Project context:
  Technology: {repo_analysis.get('technology_summary', '')}
  Use Cases : {repo_analysis.get('key_use_cases', '')}
  Industries: {repo_analysis.get('industry_impact', '')}

Answer the following VC questions as the founder. Be confident, specific,
and data-driven. Each answer should be 2-4 sentences.

{questions_text}

Respond in EXACTLY this JSON format (no markdown fences, pure JSON):
{{
  "answers": [
    "<answer to Q1>",
    "<answer to Q2>",
    "<answer to Q3>",
    "<answer to Q4>",
    "<answer to Q5>"
  ]
}}
""".strip()


# ─────────────────────────────────────────────────────────────────────────────
# 4. INVESTMENT MEMO PROMPT
# ─────────────────────────────────────────────────────────────────────────────

def investment_memo_prompt(project_data: Dict[str, Any]) -> str:
    """
    Builds a prompt asking Gemini to write a structured VC investment memo.

    Args:
        project_data: combined dict of repo signals + analysis results.

    Returns:
        Formatted prompt string.
    """
    return f"""
You are a Managing Partner at a top venture capital firm.

Write a professional investment memo for the following project.
The memo will be shared with the investment committee.

Project Data:
  - Repository      : {project_data.get('repo_name', 'Unknown')}
  - Description     : {project_data.get('description', '')}
  - GitHub Stars    : {project_data.get('stars', 0):,}
  - Contributors    : {project_data.get('contributors', 0)}
  - Star Velocity   : {project_data.get('star_velocity', 0)} stars/day
  - Social Sentiment: {project_data.get('social_sentiment', 'neutral')}
  - News Mentions   : {project_data.get('news_mentions', 0)}
  - Trend Strength  : {project_data.get('trend_strength', 'Unknown')}
  - Conviction Score: {project_data.get('conviction_score', 0):.2f} / 1.00

Technology Analysis:
  {project_data.get('technology_summary', '')}

Research Insights:
  {project_data.get('research_summary', '')}

Write the memo with EXACTLY these five sections:

## Technology Overview
<What it is and how it works>

## Market Opportunity
<Total addressable market, growth drivers, timing>

## Key Signals
<Star velocity, contributor growth, sentiment, and news as investment signals>

## Risks
<Key technical, market, and competitive risks>

## Investment Recommendation
<Clear recommendation: Invest / Watch / Pass — and rationale>

Keep the memo concise but professional. This is a real investment document.
""".strip()
