# NEWS SUMMARIZER BOT

---

## PROJECT OVERVIEW

**NEWS SUMMARIZER BOT** is a Python-based automation tool that:

- Fetches the **latest news headlines** using **NewsAPI**
- Summarizes each article using **OpenAI’s GPT-3.5-Turbo**
- Loads API keys securely via a `.env` file using `python-dotenv`
- Supports **topic-based querying** with clean, modular code
- Prevents accidental commits of secret files or API keys

---

## SETUP INSTRUCTIONS

### STEP 1 — CLONE THE PROJECT

```bash
git clone https://github.com/zolo-z1west/news_summarizer_bot.git
cd news_summarizer_bot
```

---

### STEP 2 — INSTALL DEPENDENCIES

Make sure you have **Python 3.7+** installed. Then run:

```bash
pip install -r requirements.txt
```

This installs:

- `openai` – AI summarization
- `requests` – NewsAPI calls
- `python-dotenv` – for loading secrets

---

### STEP 3 — CONFIGURE API KEYS

Create a `.env` file in your project root:

```
OPENAI_API_KEY=your_openai_key_here
NEWSAPI_KEY=your_newsapi_key_here
```

> Do **not** use quotes around keys.  
> Do **not** commit this file.

---

### STEP 4 — ENSURE `.env` IS IGNORED

In your `.gitignore`, add:

```
.env
```

Check that `.env` is ignored using:

```bash
git check-ignore -v .env
```

---

### STEP 5 — RUN THE BOT

Run the project with:

```bash
python main.py
```

This fetches and summarizes **5 space-related articles** by default.

---

## CUSTOMIZE TOPIC

Open `main.py` and find:

```python
analyze_news(keyword="space", count=5)
```

Change `"space"` to:

- `"technology"`
- `"politics"`
- `"sports"`
- or use `keyword=None` for general headlines:

```python
analyze_news(keyword=None, count=5)
```

Then run again:

```bash
python main.py
```

---

## ABOUT THIS PROJECT ;

This is one of my **first projects in AI bot development**.  
I'm open to **feedback**, **collaboration**, and new opportunities to **learn**.

Follow me on Twitter:  
[https://x.com/Zolo_Atheus](https://x.com/Zolo_Atheus)
