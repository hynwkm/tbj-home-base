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


def fetch_player_game_logs(
    player_id: int, season: int | None = None, split_length: int = 0
):
    hydrate = "stats(type=[gameLog],gameType=[R])"

    if season is not None:
        hydrate = f"stats(type=[gameLog],season={season},gameType=[R])"

    data = fetch_stats_api(f"/people/{player_id}", {"hydrate": hydrate})

    people = data.get("people", [])
    if not people:
        return "-", []

    person = people[0]

    position = person.get("primaryPosition", {}).get("abbreviation") or "-"

    target_group = "pitching" if position == "P" else "hitting"

    matching_group = next(
        (
            stats_group
            for stats_group in person.get("stats", [])
            if stats_group.get("group", {}).get("displayName") == target_group
            and stats_group.get("type", {}).get("displayName") == "gameLog"
        ),
        None,
    )

    stat_splits = matching_group.get("splits", []) if matching_group else []
    current_season = stat_splits[0].get("season") if stat_splits else season
    total_length = split_length + len(stat_splits)

    if total_length < 7 and current_season is not None:
        _, fetched_stat_splits = fetch_player_game_logs(
            player_id,
            int(current_season) - 1,
            total_length,
        )
        stat_splits.extend(fetched_stat_splits)

    stat_splits.sort(key=lambda split: split.get("date", ""), reverse=True)

    return position, stat_splits[:7]
