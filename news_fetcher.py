import requests
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv('NEWS_API_KEY')


def fetch_news(query, max_results=5):
    if not NEWS_API_KEY:
        print("API key is missing. Please add it to the .env file.")
        return []

    url = (
        f"https://newsapi.org/v2/everything?q={query}&pageSize={max_results}"
        f"&sortBy=publishedAt&language=en&apiKey={NEWS_API_KEY}"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError if the response code is 4xx/5xx

        articles = response.json().get("articles", [])
        if articles:
            return [
                article["title"] + "\n" + article["description"]
                for article in articles if article.get("description")
            ]
        else:
            print("No articles found.")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return []
