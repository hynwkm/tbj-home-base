from .cal_rate import calculate_rate


def parse_pitching_stats(stat):
    bf = stat.get("battersFaced", 0)

    return {
        "g_played": stat.get("gamesPlayed"),
        "g_started": stat.get("gamesStarted"),
        "ip": stat.get("inningsPitched"),
        "bf": stat.get("battersFaced"),
        "bb": stat.get("baseOnBalls"),
        "strikeouts": stat.get("strikeOuts"),
        "era": stat.get("era") or stat.get("earnedRunAverage"),
        "whip": stat.get("whip"),
        "so_pct": calculate_rate(stat.get("strikeOuts", 0), bf),
        "bb_pct": calculate_rate(stat.get("baseOnBalls", 0), bf),
        "so_9": stat.get("strikeoutsPer9Inn"),
        "bb_9": stat.get("walksPer9Inn"),
        "so_bb": stat.get("strikeoutWalkRatio"),
        "hr_allowed": stat.get("homeRuns"),
        "hr_9": stat.get("homeRunsPer9"),
    }
