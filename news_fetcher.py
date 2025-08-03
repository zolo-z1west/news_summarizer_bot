

import requests
from config import NEWSAPI_KEY, DEFAULT_NEWS_LANGUAGE, DEFAULT_NEWS_COUNTRY

# URL endpoint for NewsAPI
NEWSAPI_ENDPOINT = "https://newsapi.org/v2/top-headlines"

def fetch_top_headlines(query=None, language=DEFAULT_NEWS_LANGUAGE, country=DEFAULT_NEWS_COUNTRY, page_size=5):
    params = {
        'apiKey': NEWSAPI_KEY,
        'language': language,
        'pageSize': page_size,
    }

    if query:
        params['q'] = query
    else:
        params['country'] = country

    response = requests.get(NEWSAPI_ENDPOINT, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'ok':
            return data['articles']
        else:
            raise RuntimeError(f"NewsAPI Error: {data.get('message')}")
    else:
        raise ConnectionError(f"Failed to fetch news: HTTP {response.status_code}")

# if __name__ == "__main__":
#     articles = fetch_top_headlines(query="money")
#     for idx, article in enumerate(articles):
#         print(f"{idx + 1}. {article['title']} - {article['source']['name']}")
