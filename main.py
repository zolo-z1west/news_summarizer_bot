

from news_fetcher import fetch_top_headlines
from summarizer import summarize_text

def analyze_news(keyword=None, count=5):
    print(f"\n Fetching top {count} news articles", end="")
    if keyword:
        print(f" related to '{keyword}'...")
    else:
        print("...")

    try:
        articles = fetch_top_headlines(query=keyword, page_size=count)
    except Exception as fetch_error:
        print(f"Error fetching news: {fetch_error}")
        return

    if not articles:
        print("No articles found for the given query.")
        return

    for idx, article in enumerate(articles):
        print("\n" + "="*60)
        print(f"Headline {idx + 1}: {article.get('title', 'No Title')}")
        print(f"Source: {article.get('source', {}).get('name', 'Unknown')}")
        print(f"URL: {article.get('url', 'No URL')}")

        # Get main text for summarization: prefer content, then description
        content = article.get('content') or article.get('description') or ""
        if not content.strip():
            print("⚠️ No content available to summarize.")
            continue
        summary = summarize_text(content)

        print("\n📝 Summary:")
        print(summary if summary else "❌ Summary could not be generated.")

    print("\n" + "="*60)
    print("✅ News analysis completed.\n")

if __name__ == "__main__":
    analyze_news(keyword="space", count=5)
