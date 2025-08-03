import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def summarize_text(text, max_tokens=80):
    prompt = (
        f"Summarize the following news article in a clear, concise way:\n\n{text}\n\nSummary:"
    )

    try:
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes news articles."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.6,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        summary = completion.choices[0].message.content.strip()
        return summary
    except Exception as e:
        print(f"OpenAI API Error: {e}")
        return None



# if __name__ == "__main__":
#     sample_article = (
#         "SpaceX launched a new batch of Starlink satellites on Tuesday, marking the company's 35th mission this year. "
#         "The launch took place from Cape Canaveral, Florida, and aims to expand the Starlink internet constellation."
#     )

#     print("📰 Original Article:\n")
#     print(sample_article)

#     summary = summarize_text(sample_article)
    
#     print("\n📝 Summary:\n")
#     print(summary if summary else "❌ Failed to generate summary.")
