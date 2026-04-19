from pprint import pprint

from flask import Blueprint, render_template

from .services.players import get_player_data

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


@players_blueprint.route("/players/<int:player_id>")
def player(player_id):
    player = get_player_data(player_id)

    return render_template(
        "player.html",
        player_id=player_id,
        player=player,
        hitter_columns=PLAYER_HITTER_COLUMNS,
        pitcher_columns=PLAYER_PITCHER_COLUMNS,
    )
