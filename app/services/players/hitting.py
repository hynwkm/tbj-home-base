from .cal_rate import calculate_rate


def calculate_babip(stat):
    denominator = (
        stat.get("atBats", 0)
        - stat.get("strikeOuts", 0)
        - stat.get("homeRuns", 0)
        + stat.get("sacFlies", 0)
    )

    if not denominator:
        return None

    return round((stat.get("hits", 0) - stat.get("homeRuns", 0)) / denominator, 3)


def parse_hitting_stats(stat):
    pa = stat.get("plateAppearances", 0)
    strikeouts = stat.get("strikeOuts", 0)
    walks = stat.get("baseOnBalls", 0)

    return {
        "g_played": stat.get("gamesPlayed", 0),
        "pa": pa,
        "at_bats": stat.get("atBats", 0),
        "runs": stat.get("runs", 0),
        "hits": stat.get("hits", 0),
        "2b": stat.get("doubles", 0),
        "3b": stat.get("triples", 0),
        "hr": stat.get("homeRuns", 0),
        "s_bases": stat.get("stolenBases", 0),
        "cs": stat.get("caughtStealing", 0),
        "bb": walks,
        "strikeouts": strikeouts,
        "avg": stat.get("avg") or "-",
        "obp": stat.get("obp") or "-",
        "slg": stat.get("slg") or "-",
        "ops": stat.get("ops") or "-",
        "babip": calculate_babip(stat),
        "so_pct": calculate_rate(strikeouts, pa),
        "bb_pct": calculate_rate(walks, pa),
    }
