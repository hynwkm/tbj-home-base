from ..stats_api import fetch_stats_api


def fetch_players_data(player_ids: list[int], stat_type: str = "season"):
    data = fetch_stats_api(
        "/people",
        {
            "personIds": ",".join(str(player_id) for player_id in player_ids),
            "hydrate": f"stats(type=[{stat_type}],group=[hitting,pitching]),team,currentTeam",
        },
    )
    return data.get("people", [])


def fetch_player_data(player_id: int, stat_type: str = "season"):
    players = fetch_players_data([player_id], stat_type=stat_type)

    return players[0] if players else None
