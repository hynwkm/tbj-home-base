from pprint import pprint

from flask import Blueprint, render_template

from .services.players import get_player_data, get_player_game_logs

players_blueprint = Blueprint("players", __name__)


PLAYER_HITTER_COLUMNS = [
    {"key": "g_played", "label": "G"},
    {"key": "pa", "label": "PA"},
    {"key": "hits", "label": "H"},
    {"key": "runs", "label": "R"},
    {"key": "2b", "label": "2B"},
    {"key": "3b", "label": "3B"},
    {"key": "hr", "label": "HR"},
    {"key": "avg", "label": "AVG"},
    {"key": "obp", "label": "OBP"},
    {"key": "slg", "label": "SLG"},
    {"key": "ops", "label": "OPS"},
    {"key": "babip", "label": "BABIP"},
    {"key": "strikeouts", "label": "SO"},
    {"key": "bb", "label": "BB"},
    {"key": "so_pct", "label": "SO%"},
    {"key": "bb_pct", "label": "BB%"},
    {"key": "s_bases", "label": "SB"},
    {"key": "cs", "label": "CS"},
]

PLAYER_PITCHER_COLUMNS = [
    {"key": "g_played", "label": "G"},
    {"key": "g_started", "label": "GS"},
    {"key": "bf", "label": "BF"},
    {"key": "ip", "label": "IP"},
    {"key": "era", "label": "ERA"},
    {"key": "whip", "label": "WHIP"},
    {"key": "strikeouts", "label": "SO"},
    {"key": "bb", "label": "BB"},
    {"key": "so_pct", "label": "SO%"},
    {"key": "bb_pct", "label": "BB%"},
    {"key": "so_9", "label": "SO/9"},
    {"key": "bb_9", "label": "BB/9"},
    {"key": "so_bb", "label": "SO/BB"},
    {"key": "hr_allowed", "label": "HR"},
    {"key": "hr_9", "label": "HR/9"},
]

HITTER_RECENT_GAMES_COLUMNS = [
    {"key": "runs", "label": "R"},
    {"key": "rbi", "label": "RBI"},
    {"key": "2b", "label": "2B"},
    {"key": "home_runs", "label": "HR"},
    {"key": "s_bases", "label": "SB"},
]

PITCHER_RECENT_GAMES_COLUMNS = [
    {"key": "hits", "label": "H"},
    {"key": "home_runs", "label": "HR"},
    {"key": "bf", "label": "BF"},
    {"key": "whip", "label": "WHIP"},
    {"key": "pitches", "label": "P"},
]


@players_blueprint.route("/players/<int:player_id>")
def player(player_id):
    player = get_player_data(player_id)
    game_logs = get_player_game_logs(player_id)

    is_pitcher = player["is_pitcher"]

    if is_pitcher:
        recent_games_columns = PITCHER_RECENT_GAMES_COLUMNS
    else:
        recent_games_columns = HITTER_RECENT_GAMES_COLUMNS

    return render_template(
        "player.html",
        player_id=player_id,
        player=player,
        hitter_columns=PLAYER_HITTER_COLUMNS,
        pitcher_columns=PLAYER_PITCHER_COLUMNS,
        game_logs=game_logs,
        recent_games_columns=recent_games_columns,
    )
