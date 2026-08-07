import requests
import trafilatura


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

url = input("Enter the URL of the article: ")

article = extract_article(url)

if article:
    print(article)