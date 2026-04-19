from ..utils import player_headshot_url
from .stats_api import fetch_stats_api
from .teams import get_team_lookup

LEADER_LABELS = {
    "homeRuns": "Home Runs",
    "onBasePlusSlugging": "OPS",
    "strikeouts": "Strikeouts",
    "earnedRunAverage": "ERA",
}


LEADER_ORDER = [
    "homeRuns",
    "onBasePlusSlugging",
    "strikeouts",
    "earnedRunAverage",
]


def parse_leaderboard(league_leaders, team_lookup):
    leaders_by_category = {}

    for leader in league_leaders:
        category = leader.get("leaderCategory")
        if category not in leaders_by_category:
            leaders_by_category[category] = leader

    parsed_leaderboard = []

    for category in LEADER_ORDER:
        leaderboard = leaders_by_category.get(category)
        if not leaderboard:
            continue

        leaders = leaderboard.get("leaders", [])
        if not leaders:
            continue

        top_leader = leaders[0]
        team_id = top_leader.get("team", {}).get("id")
        player_id = top_leader.get("person", {}).get("id")

        parsed_leaderboard.append(
            {
                "category": category,
                "label": LEADER_LABELS.get(category, category),
                "value": top_leader.get("value"),
                "team_id": team_id,
                "player_id": player_id,
                "team_initials": team_lookup.get(team_id, {}).get("abbreviation", ""),
                "player_name": top_leader.get("person", {}).get("fullName", ""),
                "headshot_url": player_headshot_url(player_id),
            }
        )

    return parsed_leaderboard


def get_stat_leaders():
    team_lookup = get_team_lookup()
    data = fetch_stats_api(
        "/stats/leaders",
        {
            "leaderCategories": "homeRuns,onBasePlusSlugging,strikeouts,earnedRunAverage",
            "statGroup": "hitting,pitching",
        },
    )

    return parse_leaderboard(data.get("leagueLeaders", []), team_lookup)


def get_team_leaders(team_id):
    team_lookup = get_team_lookup()
    data = fetch_stats_api(
        f"/teams/{team_id}/leaders",
        {
            "leaderCategories": "homeRuns,onBasePlusSlugging,strikeouts,earnedRunAverage",
            "statGroup": "hitting,pitching",
        },
    )

    return parse_leaderboard(data.get("teamLeaders", []), team_lookup)
