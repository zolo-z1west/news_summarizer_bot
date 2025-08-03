**News Summarizer Bot**
```

## Specifications

This project is a Python-based bot that:

- Fetches the latest news headlines using NewsAPI.
- Summarizes each news article using OpenAI's Chat API (`gpt-3.5-turbo`).
- Loads API keys securely from a `.env` file using the `python-dotenv` package.
- Supports topic-based querying and modular logic.
- Avoids committing any secret files or keys to Git.

## Setup Instructions

### 1. Clone the Project

```bash
git clone https://github.com/your-username/news_summarizer_bot.git
cd news_summarizer_bot
```


### 2. Install Dependencies

Ensure you have Python 3.7+ installed. From your project folder, run:

```bash
pip install -r requirements.txt
```

This installs:

- `openai` – for AI summarization
- `requests` – to call NewsAPI
- `python-dotenv` – to safely load secrets from `.env`

### 3. Add Your API Keys (⚠ Do Not Share)

Create a `.env` file in your project root with the following contents:

```
OPENAI_API_KEY=your_openai_key_here
NEWSAPI_KEY=your_newsapi_key_here
```

- Do **not** wrap keys in quotes.
- Do **not** commit this file to GitHub.

### 4. Add `.env` to `.gitignore`

Make sure `.gitignore` includes:

```
.env
```

This prevents accidental commit of secrets (which would trigger GitHub push protection errors).

### 5. Run the Bot

To run the project and see news summaries:

```bash
python main.py
```

This will fetch and summarize five articles (default topic is "space").

## Changing the News Topic

To update the type of news being summarized:

1. Open `main.py`
2. Locate the line:

   ```python
   analyze_news(keyword="space", count=5)
   ```

3. Change `"space"` to your preferred topic, like `"technology"`, `"politics"`, or `"sports"`, for example:

   ```python
   analyze_news(keyword="technology", count=5)
   ```

4. You can also set `keyword=None` to fetch general top headlines:

   ```python
   analyze_news(keyword=None, count=5)
   ```

5. Save and rerun:

   ```bash
   python main.py
   ```

## Troubleshooting

- **No news articles returned**: Try using a general keyword or set `keyword=None`.
- **Push blocked by GitHub**: Remove secrets from `.env`, clean history with `git filter-repo`, and force push only after `.env` is excluded.
- **Summary shows as `None`**: Check that your OpenAI key is valid and that `openai` package is using the new `chat.completions.create()` format.

## Security Reminders

- Never commit actual API keys.
- Always test `.gitignore` to confirm `.env` is ignored:  
  ```bash
  git check-ignore -v .env
  ```


This is one of my first projects in ai bot creation. I would love feedbacks and any oppurtunities of collaborating and learning.

Follow my twitter (i post regularly while i create new projs).
https://x.com/Zolo_Atheus