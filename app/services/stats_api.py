import requests

from config import MLB_STATS_API_BASE_URL


def fetch_stats_api(path, params=None):
    url = f"{MLB_STATS_API_BASE_URL}{path}"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
