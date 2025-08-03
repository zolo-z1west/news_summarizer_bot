

import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

DEFAULT_NEWS_LANGUAGE = "en"
DEFAULT_NEWS_COUNTRY = "us"
