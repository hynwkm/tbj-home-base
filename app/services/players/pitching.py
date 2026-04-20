from .cal_rate import calculate_rate


def parse_pitching_stats(stat):
    bf = stat.get("battersFaced", 0)

    return {
        "g_played": stat.get("gamesPlayed", 0),
        "g_started": stat.get("gamesStarted", 0),
        "ip": stat.get("inningsPitched") or "-",
        "bf": stat.get("battersFaced", 0),
        "bb": stat.get("baseOnBalls", 0),
        "strikeouts": stat.get("strikeOuts", 0),
        "era": stat.get("era") or stat.get("earnedRunAverage") or "-",
        "whip": stat.get("whip") or "-",
        "so_pct": calculate_rate(stat.get("strikeOuts", 0), bf),
        "bb_pct": calculate_rate(stat.get("baseOnBalls", 0), bf),
        "so_9": stat.get("strikeoutsPer9Inn") or "-",
        "bb_9": stat.get("walksPer9Inn") or "-",
        "so_bb": stat.get("strikeoutWalkRatio") or "-",
        "hr_allowed": stat.get("homeRuns", 0),
        "hr_9": stat.get("homeRunsPer9") or "-",
        "ops": stat.get("ops") or "-",
    }
