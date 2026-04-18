from datetime import datetime

import feedparser
import requests
from bs4 import BeautifulSoup

from config import MLB_NEWS_RSS_URL, TIMEOUT


def format_published_at(epoch_str):
    if not epoch_str:
        return ""

    dt = datetime.fromtimestamp(int(epoch_str))
    time = dt.strftime("%I:%M %p").lstrip("0")
    year = str(dt.year)[2:]

    return f"{dt.month}/{dt.day}/{year} — {time}"


def get_mlb_news():
    response = requests.get(f"{MLB_NEWS_RSS_URL}feeds/news/rss.xml", timeout=TIMEOUT)
    response.raise_for_status()

    feed = feedparser.parse(response.content)
    soup = BeautifulSoup(response.content, "xml")

    items = soup.find_all("item")[:8]
    entries = feed.entries[:8]

    articles = []

    for entry, item in zip(entries, items):
        image = item.find("image")
        image_url = image.get("href", "") if image else ""

        epoch_tag = item.find("mlb:display-date-epoch")

        epoch_value = epoch_tag.text if epoch_tag else ""

        articles.append(
            {
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "published_at": format_published_at(epoch_value),
                "author": entry.get("author", ""),
                "image_url": image_url,
            }
        )

    return articles
