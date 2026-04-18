from .stats_api import fetch_stats_api


def get_team_abbreviations():
    data = fetch_stats_api("/teams", {"sportId": "1"})

    return {team["id"]: team["abbreviation"] for team in data["teams"]}
