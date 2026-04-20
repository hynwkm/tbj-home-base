from .cal_rate import calculate_rate


def is_reliever(g_played, g_started, ip):
    if not ip or ip == "-":
        ip = 0.0
    innings, _, outs = str(ip).partition(".")
    innings = int(innings)
    if outs == "1":
        innings += 1 / 3
    elif outs == "2":
        innings += 2 / 3

    gs_per_game = g_started / g_played if g_played else 0
    ip__per_game = innings / g_played if g_played else 0

    return gs_per_game <= 0.20 and ip__per_game <= 2.0


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
        "is_reliever": is_reliever(
            stat.get("gamesPlayed", 0),
            stat.get("gamesStarted", 0),
            stat.get("inningsPitched"),
        ),
    }
