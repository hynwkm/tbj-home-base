from .stats_api import fetch_stats_api
from .teams import get_team_abbreviations


def parse_team_record(team_record, team_abbreviations):
    team = team_record.get("team", {})
    splits = team_record.get("records", {}).get("splitRecords", [])
    l10_record = next((item for item in splits if item.get("type") == "lastTen"), {})

    return {
        "team_id": team.get("id"),
        "team_name": team.get("name"),
        "team_abbreviation": team_abbreviations.get(team.get("id")),
        "wins": team_record.get("wins"),
        "losses": team_record.get("losses"),
        "pct": team_record.get("winningPercentage"),
        "gb": team_record.get("gamesBack"),
        "l10": f"{l10_record.get('wins', 0)}-{l10_record.get('losses', 0)}",
        "diff": team_record.get("runDifferential"),
    }


DIVISION_NAMES = {
    200: "AL West",
    201: "AL East",
    202: "AL Central",
    203: "NL West",
    204: "NL East",
    205: "NL Central",
}


def get_division_standings():
    data = fetch_stats_api("/standings", {"leagueId": "103,104"})
    team_abbreviatons = get_team_abbreviations()

    divisions = []

    for record_group in data.get("records", []):
        division_info = record_group.get("division", {})
        division_id = division_info.get("id")
        team_records = record_group.get("teamRecords", [])

        divisions.append(
            {
                "division_id": division_info.get("id"),
                "division_name": DIVISION_NAMES.get(division_id),
                "teams": [
                    parse_team_record(team, team_abbreviatons) for team in team_records
                ],
            }
        )

    return divisions
