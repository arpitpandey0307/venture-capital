import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

class Settings:

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL = "gemini-2.5-flash-lite"

    EXA_API_KEY = os.getenv("EXA_API_KEY")
    EXA_NUM_RESULTS = 5

    MONGO_URI = os.getenv("MONGO_URI")

    MONGO_DB_NAME = "venture_alpha"
    MONGO_COLLECTION_SIGNALS = "signals"

    APP_TITLE = "Venture-Alpha AI Intelligence Layer"
    APP_VERSION = "1.0.0"
    APP_DESCRIPTION = (
        "AI reasoning service that transforms structured repository signals "
        "into investment-grade insights using Gemini 2.0 Flash and Exa Search."
    )

    def validate(self):
        if not self.GEMINI_API_KEY:
            raise Exception("GEMINI_API_KEY missing in .env")

        if not self.EXA_API_KEY:
            raise Exception("EXA_API_KEY missing in .env")

        if not self.MONGO_URI:
            raise Exception("MONGO_URI missing in .env")


settings = Settings()

mongo_client = MongoClient(settings.MONGO_URI)
mongo_db = mongo_client[settings.MONGO_DB_NAME]
signals_collection = mongo_db[settings.MONGO_COLLECTION_SIGNALS]

print("Gemini key loaded:", settings.GEMINI_API_KEY[:10])