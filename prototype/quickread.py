import requests
import trafilatura
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

if not api_key:
    raise ValueError("OPENROUTER_API_KEY is missing.")

def extract_article(url):
    response = requests.get(url)

    if response.status_code !=200:
        print("Could not retrieve the webpage.")
        return None


    article_text = trafilatura.extract(
        response.text,
        include_comments=False,
        include_tables=False,
    )

    if not article_text:
        print("Could not extract article text from the provided URL.")
        return None

    return article_text

def summarize_article(article_text):
    prompt = f"""
You are QuickRead, a document analysis assistant.

Your task is to extract the most important information from an article.

Rules:
- Use only information from the article.
- Do not add assumptions, opinions, or outside information.
- Use simple, clear language.
- Avoid unnecessary jargon.
- Remove repeated information.
- Focus on facts, not explanations.
- Do not write conclusions or implications.
- Do not summarize the article’s overall meaning.
- Extract only direct facts.

Selection rules:
- Include only facts necessary to understand the article.
- Remove minor background details.
- Prioritize the main event, causes, responses, and outcomes.
- Do not list every detail mentioned in the article.

Fact selection:
- Prioritize facts that explain what happened, why it happened, who is involved, and what happens next.
- Remove minor background details unless they affect the main story.

Output format:

Overview:
- Write exactly one sentence.
- Prefer short sentences under 20 words.
- Describe only the main topic.

- Write 5-8 bullet points covering the most important facts.
- Include only information necessary to understand the article.
- Do not add filler facts to reach a specific number.
- Each bullet should contain one fact.
- Each bullet should be one sentence.
- Keep bullets short.

Article:
{article_text}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

url = input("Enter the URL of the article: ")

article = extract_article(url)

if article:
    summary = summarize_article(article)
    print(summary)