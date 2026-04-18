import requests

from config import MLB_STATS_API_BASE_URL, TIMEOUT

session = requests.Session()


def fetch_stats_api(path, params=None):
    url = f"{MLB_STATS_API_BASE_URL}{path}"
    response = session.get(url, params=params, timeout=TIMEOUT)
    response.raise_for_status()
    return response.json()
