"""
tools/research_tool.py
-----------------------
Tool 2 — Web Research Validator

Steps:
  1. Query Exa Search API with repo_name + contextual keywords
  2. Retrieve top-N article titles and URLs
  3. Summarise insights using Gemini (google.genai SDK)
"""

import logging
from typing import Dict, Any, List

import requests
from google import genai

from config import settings
from models.schemas import ResearchOutput

logger = logging.getLogger(__name__)

# Initialise the new google.genai client
_client = genai.Client(api_key=settings.GEMINI_API_KEY)

# Exa Search API endpoint
EXA_SEARCH_URL = "https://api.exa.ai/search"


def _search_exa(query: str) -> List[Dict[str, Any]]:
    """
    Query the Exa Search API and return a list of result objects.

    Args:
        query: Search query string.

    Returns:
        List of result dicts (up to EXA_NUM_RESULTS).
    """
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-api-key": settings.EXA_API_KEY
    }
    payload = {
        "query": query,
        "numResults": settings.EXA_NUM_RESULTS,
        "type": "neural",
        "useAutoprompt": True,
        "contents": {
            "text": {
                "maxCharacters": 500
            }
        }
    }

    response = requests.post(EXA_SEARCH_URL, headers=headers, json=payload, timeout=15)
    response.raise_for_status()

    results = response.json().get("results", [])
    logger.info(f"Exa returned {len(results)} results for query: '{query}'")
    return results


def _summarise_with_gemini(repo_name: str, articles: List[Dict[str, Any]]) -> str:
    """
    Ask Gemini to synthesise insights from article snippets.

    Args:
        repo_name: Name of the repository/technology.
        articles:  List of Exa result dicts.

    Returns:
        Plain-text research summary string.
    """
    articles_text = ""
    for i, art in enumerate(articles, 1):
        title = art.get("title", "Untitled")
        snippet = (art.get("text") or "No snippet available.")[:400]
        articles_text += f"\n[Article {i}] {title}\n{snippet}\n"

    prompt = f"""
You are a technology research analyst.

Based on the following web articles about "{repo_name}", write a concise
3-5 sentence research summary highlighting:
  • Current industry adoption trends
  • Developer community reception
  • Any notable companies or projects using it
  • Market positioning vs. alternatives

Articles:
{articles_text}

Respond with plain text only (no JSON, no headers, no bullet points).
""".strip()

    response = _client.models.generate_content(
        model=settings.GEMINI_MODEL,
        contents=prompt
    )
    return response.text.strip()


def research_technology(repo_name: str) -> ResearchOutput:
    """
    Search Exa for recent articles about the technology, then
    use Gemini to synthesise the findings into an investment-relevant summary.

    Args:
        repo_name: Name of the repository (e.g. "LangGraph").

    Returns:
        ResearchOutput with research_summary and sources list.
    """
    logger.info(f"Researching technology: {repo_name}")

    search_query = (
        f"{repo_name} open source technology developer adoption "
        f"venture capital investment startup 2024 2025"
    )

    try:
        articles = _search_exa(search_query)
    except requests.RequestException as e:
        logger.warning(f"Exa search failed: {e}. Returning empty research.")
        return ResearchOutput(
            research_summary="Web research unavailable due to API error.",
            sources=[]
        )

    sources = [art.get("url", "") for art in articles if art.get("url")]

    if articles:
        summary = _summarise_with_gemini(repo_name, articles)
    else:
        summary = f"No external articles found for '{repo_name}'."

    return ResearchOutput(
        research_summary=summary,
        sources=sources
    )
