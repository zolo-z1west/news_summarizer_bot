**News Summarizer Bot**
```

## Specifications

This Python-based bot:

- Fetches current news headlines using the NewsAPI.
- Summarizes each article using OpenAI's GPT model (gpt-3.5-turbo by default).
- Uses environment variables for API keys, loaded via the `python-dotenv` package.
- Is modular and easy to adapt or extend.

## Setup Instructions

### 1. Clone the Project Repository
If hosted on GitHub (or adapt as needed for your workflow):

```bash
git clone https://github.com/your-username/news-summarizer-bot.git
cd news-summarizer-bot
```

### 2. Install Dependencies
Ensure you have Python 3.7 or higher installed. Then install required packages:

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` File for Secrets
Create a file named `.env` in the root of your project with the following content:

```
OPENAI_API_KEY=your_openai_api_key_here
NEWSAPI_KEY=your_newsapi_key_here
```

Replace the values with your actual API keys.

### 4. Add `.env` to `.gitignore` (optional but recommended)
To prevent accidental exposure of sensitive info, make sure `.env` is listed in `.gitignore`:

```
.env
```

> This step may already be reflected in your project.

## Running the Bot

To run the bot and see result summaries:

```bash
python main.py
```

This will fetch and summarize 5 recent news articles using default settings.

## Changing the News Query

The default behavior fetches news headlines using the keyword `"space"` (or general headlines if set to `None`).

To change this:

1. Open `main.py`
2. Locate the line:

   ```python
   analyze_news(keyword="space", count=5)
   ```

3. Replace `"space"` with any topic of your choice:

   ```python
   analyze_news(keyword="technology", count=5)
   analyze_news(keyword="sports", count=3)
   ```

4. You may also set `keyword=None` to fetch general top headlines:

   ```python
   analyze_news(keyword=None, count=5)
   ```

5. Save and re-run:

   ```bash
   python main.py
   ```

## Notes

- OpenAI key requires an active OpenAI account with access to `gpt-3.5-turbo`.
- NewsAPI.org keys are free to obtain with limited usage per day.
- Output includes each article’s title, source, URL, and summarized content.

Let me know if you’d like this README exported to a `.md` file or want to add project badges, screenshots, CLI options, or deployment steps.
