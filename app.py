from news_fetcher import fetch_news
from summarizer import summarize_article
import datetime
import os


def main():
    query = input("Enter your news topic: ")
    news_articles = fetch_news(query)

    if not news_articles:
        print("No articles found.")
        return

    # Create logs directory if not exists
    os.makedirs("logs", exist_ok=True)

    # Timestamped filename
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"logs/summary_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        for idx, article in enumerate(news_articles, start=1):
            summary = summarize_article(article)
            f.write(f"Article {idx}:\n")
            f.write(f"Original: {article}\n")
            f.write(f"Summary: {summary}\n")
            f.write("=" * 80 + "\n\n")

            # Also print to console
            print(f"\nArticle {idx}:")
            print(f"Original: {article}")
            print(f"Summary: {summary}")
            print("=" * 80)

    print(f"\n✅ Summaries saved to {filename}")


if __name__ == "__main__":
    main()
