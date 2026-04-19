from .stats_api import fetch_stats_api


def get_player_data(player_id):
    data = fetch_stats_api(
        f"/people/{player_id}?hydrate=stats(type=[yearByYear,yearByYearAdvanced,projected,career]),team,currentTeam"
    )


def calculate_rate(numerator, denominator, digits=3):
    if not denominator:
        return None
    return round(numerator / denominator, digits)


def calculate_babip(stat):
    denominator = (
        stat.get("atBats", 0)
        - stat.get("strikeOuts", 0)
        - stat.get("homeRuns", 0)
        + stat.get("sacFlies", 0)
    )

    if not denominator:
        return None

    return round(
        (stat.get("hits", 0) - stat.get("homeRuns", 0)) / denominator,
        3,
    )


def parse_hitting_stats(stat):
    pa = stat.get("plateAppearances", 0)

    return {
        "g_played": stat.get("gamesPlayed"),
        "pa": stat.get("plateAppearances"),
        "at_bats": stat.get("atBats"),
        "runs": stat.get("runs"),
        "hits": stat.get("hits"),
        "2b": stat.get("doubles"),
        "3b": stat.get("triples"),
        "hr": stat.get("homeRuns"),
        "s_bases": stat.get("stolenBases"),
        "cs": stat.get("caughtStealing"),
        "bb": stat.get("baseOnBalls"),
        "strikeouts": stat.get("strikeOuts"),
        "avg": stat.get("avg"),
        "obp": stat.get("obp"),
        "slg": stat.get("slg"),
        "ops": stat.get("ops"),
        "babip": calculate_babip(stat),
        "so_pct": calculate_rate(stat.get("strikeOuts", 0), pa),
        "bb_pct": calculate_rate(stat.get("baseOnBalls", 0), pa),
    }


def parse_pitching_stats(stat):
    bf = stat.get("battersFaced", 0)

    return {
        "g_played": stat.get("gamesPlayed"),
        "ip": stat.get("inningsPitched"),
        "bf": stat.get("battersFaced"),
        "bb": stat.get("baseOnBalls"),
        "strikeouts": stat.get("strikeOuts"),
        "era": stat.get("era") or stat.get("earnedRunAverage"),
        "so_pct": safe_rate(stat.get("strikeOuts", 0), bf),
        "bb_pct": safe_rate(stat.get("baseOnBalls", 0), bf),
    }


def parse_stats_by_group(stats_groups):
    stats_by_group = {}

    for stats_group in stats_groups:
        group = stats_group.get("group", {}).get("displayName")
        splits = stats_group.get("splits", [])

        if not splits:
            continue

        stat = splits[0].get("stat", {})

        if group == "hitting":
            stats_by_group["hitting"] = parse_hitting_stats(stat)
        elif group == "pitching":
            stats_by_group["pitching"] = parse_pitching_stats(stat)

    return stats_by_group


def parse_player_bio(player):
    position = player.get("primaryPosition", {}).get("abbreviation")

    return {
        "player_id": player.get("id"),
        "last_first_name": player.get("lastFirstName"),
        "jersey_number": player.get("primaryNumber"),
        "position": position,
        "is_pitcher": position == "P",
        "age": player.get("currentAge"),
        "height": player.get("height"),
        "weight": player.get("weight"),
        "draft_year": player.get("draftYear"),
        "b_side": player.get("batSide", {}).get("code"),
        "t_hand": player.get("pitchHand", {}).get("code"),
    }


def parse_player(player):
    stats_by_group = parse_stats_by_group(player.get("stats", []))

    return {
        **parse_player_bio(player),
        "hitting_stats": stats_by_group.get("hitting", []),
        "pitching_stats": stats_by_group.get("pitching", []),
    }


def get_players_data(player_ids: list[int], stat_types: str = "season"):
    data = fetch_stats_api(
        "/people",
        {
            "personIds": ",".join(str(player_id) for player_id in player_ids),
            "hydrate": f"stats(type=[{stat_types}],group=[hitting,pitching]),team,currentTeam",
        },
    )
    return [parse_player(player) for player in data.get("people", [])]


def get_current_season_roster_data(player_ids: list[int]):
    return get_players_data(player_ids, stat_types="season")
