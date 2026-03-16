"""
config.py
---------
Centralised configuration loader for Venture-Alpha AI module.
Reads API keys and settings from environment variables (via .env file).
"""

import os
from dotenv import load_dotenv

# Load variables from .env file into the environment
load_dotenv()


class Settings:
    """Application-wide settings loaded from environment variables."""

    # ── Google Gemini 1.5 Flash ──────────────────────────────────────────────
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL: str = "gemini-2.0-flash"   # free-tier model (new google.genai SDK)

    # ── Exa Search API ───────────────────────────────────────────────────────
    EXA_API_KEY: str = os.getenv("EXA_API_KEY", "")
    EXA_NUM_RESULTS: int = 5                  # top-N articles to fetch

    # ── FastAPI app meta ─────────────────────────────────────────────────────
    APP_TITLE: str = "Venture-Alpha AI Intelligence Layer"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = (
        "AI reasoning service that transforms structured repository signals "
        "into investment-grade insights using Gemini 1.5 Flash and Exa Search."
    )

    def validate(self) -> None:
        """Raise if required keys are missing."""
        if not self.GEMINI_API_KEY:
            raise EnvironmentError("GEMINI_API_KEY is not set in .env")
        if not self.EXA_API_KEY:
            raise EnvironmentError("EXA_API_KEY is not set in .env")


# Singleton instance used throughout the project
settings = Settings()
