from .hitting import parse_hitting_stats
from .pitching import parse_pitching_stats


def parse_player_bio(player):
    position = player.get("primaryPosition", {}).get("abbreviation")

    return {
        "player_id": player.get("id"),
        "last_first_name": player.get("lastFirstName"),
        "initials": player.get("lastInitName"),
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


def parse_stats_by_group(stats_groups: list):
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


def parse_player(player):
    person = player.get("person", {})
    stats_groups: list = person.get("stats", [])

    stats_by_group = parse_stats_by_group(stats_groups)

    return {
        **parse_player_bio(person),
        "hitting_stats": stats_by_group.get("hitting", []),
        "pitching_stats": stats_by_group.get("pitching", []),
    }
