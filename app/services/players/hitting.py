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
