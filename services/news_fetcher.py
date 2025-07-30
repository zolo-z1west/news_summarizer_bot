# news_fetch.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_news():
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        articles = data.get("articles", [])
        return articles
    else:
        raise Exception(f"NewsAPI Error: {data.get('message')}")

def get_news_summary(articles):
    summaries = []
    for article in articles:
        title = article.get("title", "")
        description = article.get("description", "")
        summary = f"📰 {title}\n{description}\n"
        summaries.append(summary)
    return summaries# news_fetch.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_news():
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    response = requests.get(url)
    data = response.json() #fill the json responses into a dictionary

    if response.status_code == 200:
        articles = data.get("articles", [])
        return articles
    else:
        raise Exception(f"NewsAPI Error: {data.get('message')}")

def get_news_summary(articles):
    summaries = []
    for article in articles:
        title = article.get("title", "")
        description = article.get("description", "")
        summary = f"📰 {title}\n{description}\n"
        summaries.append(summary)
    return summaries