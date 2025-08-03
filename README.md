**News Summarizer Bot**
```

## Specifications

This is a Python-based bot that:

- Fetches current news headlines using the NewsAPI.
- Summarizes each article using OpenAI's GPT model (gpt-3.5-turbo by default).
- Returns brief summaries alongside article headlines and source information.
- Is modular and easy to extend or customize.

## Setup Instructions

1. **Clone the repository**  
   (If you have the project on GitHub or in a repository)

   ```
   git clone https://github.com/zolo-z1west/news-summarizer-bot.git
   cd news-summarizer-bot
   ```

2. **Install required packages**

   Make sure you have Python 3.7 or above installed. Then run:

   ```
   pip install -r requirements.txt
   ```

3. **Add your API keys**

   Open the `config.py` file and add your keys:

   ```python
   OPENAI_API_KEY = "your_openai_api_key"
   NEWSAPI_KEY = "your_newsapi_api_key"
   ```

4. **Run the bot**

   You can start the bot by running:

   ```
   python main.py
   ```

## Customizing the News Query

To change what kind of news is fetched:

1. Open the `main.py` file.
2. Find the line:

   ```python
   analyze_news(keyword="space", count=5)
   ```

3. Replace `"space"` with any keyword of your choice (for example, `"sports"`, `"politics"`, `"science"`).

4. You can also set the keyword to `None` to fetch general top headlines:

   ```python
   analyze_news(keyword=None, count=5)
   ```

5. Save the file and rerun:

   ```
   python main.py
   ```

This will fetch and summarize new articles based on the keyword you set.
