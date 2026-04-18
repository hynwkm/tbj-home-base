from .stats_api import fetch_stats_api
from .teams import get_team_lookup


def parse_team_record(team_record, team_info):
    team = team_record.get("team", {})
    splits = team_record.get("records", {}).get("splitRecords", [])
    l10_record = next((item for item in splits if item.get("type") == "lastTen"), {})
    home_record = next((item for item in splits if item.get("type") == "home"), {})
    away_record = next((item for item in splits if item.get("type") == "away"), {})
    one_run_record = next((item for item in splits if item.get("type") == "oneRun"), {})
    extra_inn_record = next(
        (item for item in splits if item.get("type") == "extraInning"), {}
    )

    return {
        "team_id": team.get("id"),
        "team_name": team.get("name"),
        "team_full_name": team_info.get(team.get("id")).get("full_name"),
        "team_abbreviation": team_info.get(team.get("id")).get("abbreviation"),
        "wins": team_record.get("wins"),
        "losses": team_record.get("losses"),
        "pct": team_record.get("winningPercentage"),
        "gb": team_record.get("gamesBack"),
        "l10": f"{l10_record.get('wins', 0)}-{l10_record.get('losses', 0)}",
        "diff": team_record.get("runDifferential"),
        "home_pct": home_record.get("pct", ""),
        "away_pct": away_record.get("pct", ""),
        "1run_pct": one_run_record.get("pct", ""),
        "xtra_inn_pct": extra_inn_record.get("pct", ""),
        "division_rank": team_record.get("divisionRank"),
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
    team_info = get_team_lookup()

    divisions = []

    for record_group in data.get("records", []):
        division_info = record_group.get("division", {})
        division_id = division_info.get("id")
        team_records = sorted(
            record_group.get("teamRecords", []),
            key=lambda team: int(team.get("divisionRank", 999)),
        )
        divisions.append(
            {
                "division_id": division_info.get("id"),
                "division_name": DIVISION_NAMES.get(division_id),
                "teams": [parse_team_record(team, team_info) for team in team_records],
            }
        )

    return divisions


def get_team_standing_info(team_id):
    division_standings = get_division_standings()

    for division in division_standings:
        for team in division["teams"]:
            if team["team_id"] == team_id:
                return {
                    **team,
                    "division_id": division["division_id"],
                    "division_name": division["division_name"],
                }

    return None
