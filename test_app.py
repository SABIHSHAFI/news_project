# test_app.py
import os
import pytest
from news_fetcher import fetch_news
from dotenv import load_dotenv

load_dotenv()

def test_fetch_news():
    query = "technology"  # Change this based on what you want to test
    result = fetch_news(query)

    # Check that the result is not empty
    assert len(result) > 0, "No news articles returned!"
