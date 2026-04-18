from .stats_api import fetch_stats_api


def get_teams():
    data = fetch_stats_api("/teams", {"sportId": "1"})
    return data.get("teams", [])


def get_team_lookup():
    teams = get_teams()

    return {
        team["id"]: {
            "abbreviation": team["abbreviation"],
            "name": team["teamName"],
            "full_name": team["name"],
        }
        for team in teams
    }
