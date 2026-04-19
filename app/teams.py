from flask import Blueprint, render_template

from .services.mlb_news import get_team_news
from .services.standings import get_team_standing_info
from .services.teams import get_team_roster_stats

teams_blueprint = Blueprint("teams", __name__)


HITTER_COLUMNS = [
    {"key": "age", "label": "Age"},
    {"key": "b_side", "label": "B"},
    {"key": "t_hand", "label": "T"},
    {"key": "pa", "label": "PA"},
    {"key": "hits", "label": "H"},
    {"key": "2b", "label": "2B"},
    {"key": "3b", "label": "3B"},
    {"key": "hr", "label": "HR"},
    {"key": "s_bases", "label": "SB"},
    {"key": "so_pct", "label": "SO%"},
    {"key": "bb_pct", "label": "BB%"},
    {"key": "avg", "label": "AVG"},
    {"key": "obp", "label": "OBP"},
    {"key": "ops", "label": "OPS"},
]

PITCHER_COLUMNS = [
    {"key": "age", "label": "Age"},
    {"key": "g_played", "label": "G"},
    {"key": "ip", "label": "IP"},
    {"key": "bf", "label": "BF"},
    {"key": "era", "label": "ERA"},
    {"key": "strikeouts", "label": "SO"},
    {"key": "bb", "label": "BB"},
    {"key": "so_pct", "label": "SO%"},
    {"key": "bb_pct", "label": "BB%"},
    {"key": "ops", "label": "OPS"},
]


@teams_blueprint.route("/teams/<int:team_id>")
def team(team_id):

    team_info = get_team_standing_info(team_id)
    roster_info = get_team_roster_stats(team_id)
    team_slug = team_info["team_name"].replace(" ", "").lower()

    return render_template(
        "team.html",
        team_info=team_info,
        hitters=roster_info["hitters"],
        pitchers=roster_info["pitchers"],
        HITTER_COLUMNS=HITTER_COLUMNS,
        PITCHER_COLUMNS=PITCHER_COLUMNS,
        team_news=get_team_news(team_slug),
    )
