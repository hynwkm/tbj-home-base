from .hitting import parse_hitting_stats
from .pitching import parse_pitching_stats


def parse_player_bio(player):
    position = player.get("primaryPosition", {}).get("abbreviation") or "-"

    return {
        "player_id": player.get("id"),
        "last_first_name": player.get("lastFirstName") or "-",
        "initials": player.get("lastInitName") or "-",
        "jersey_number": player.get("primaryNumber"),
        "current_team_name": player.get("currentTeam", {}).get("name") or "-",
        "position": position,
        "is_pitcher": position == "P",
        "age": player.get("currentAge"),
        "height": player.get("height") or "-",
        "weight": player.get("weight") or "-",
        "draft_year": player.get("draftYear") or "-",
        "b_side": player.get("batSide", {}).get("code") or "-",
        "t_hand": player.get("pitchHand", {}).get("code") or "-",
    }


def parse_stats_by_group(stats_groups: list):
    stats_by_group = {
        "hitting": {},
        "pitching": {},
    }

    for stats_group in stats_groups:
        group = stats_group.get("group", {}).get("displayName").lower()
        stat_type = stats_group.get("type", {}).get("displayName")
        splits = stats_group.get("splits", [])

        if group not in ["hitting", "pitching"] or not splits:
            continue

        stats_by_group.setdefault(group, {})

        parser = parse_hitting_stats if group == "hitting" else parse_pitching_stats

        if stat_type in ["season", "career", "projected"]:
            split = splits[0]
            stat = split.get("stat", {})

            stats_by_group[group][stat_type] = {
                "season": split.get("season"),
                **parser(stat),
            }
        elif stat_type in ["yearByYear", "yearByYearAdvanced"]:
            stats_by_group[group][stat_type] = [
                {
                    "season": split.get("season"),
                    "team_name": split.get("team", {}).get("name"),
                    "team_id": split.get("team", {}).get("id"),
                    **parser(split.get("stat", {})),
                }
                for split in splits
            ]

    return stats_by_group


def parse_player(player):
    if "person" in player:
        person = player["person"]
    else:
        person = player

    stats_groups: list = person.get("stats", [])

    stats_by_group = parse_stats_by_group(stats_groups)

    return {
        **parse_player_bio(person),
        "hitting_stats": stats_by_group.get("hitting", {}),
        "pitching_stats": stats_by_group.get("pitching", {}),
    }
