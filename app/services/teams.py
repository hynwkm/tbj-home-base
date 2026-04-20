from .players import parse_player
from .stats_api import fetch_stats_api


def get_teams():
    data = fetch_stats_api("/teams", {"sportId": "1"})
    return data.get("teams", [])


def get_team_lookup():
    teams = get_teams()

    return {
        team["id"]: {
            "team_id": team["id"],
            "abbreviation": team["abbreviation"],
            "name": team["teamName"],
            "full_name": team["name"],
        }
        for team in teams
    }


def get_team_roster_stats(team_id):
    data = fetch_stats_api(
        f"/teams/{team_id}/roster/Active",
        {"hydrate": "person(stats(type=season))"},
    )
    roster = data.get("roster", [])

    roster_stats = [parse_player(player) for player in roster]

    hitters = [player for player in roster_stats if not player["is_pitcher"]]
    pitchers = [player for player in roster_stats if player["is_pitcher"]]

    return {
        "hitters": hitters,
        "pitchers": pitchers,
    }
