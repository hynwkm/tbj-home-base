from flask import Blueprint, render_template

from .services.leaderboard import get_stat_leaders
from .services.mlb_news import get_mlb_news
from .services.standings import get_division_standings

home_blueprint = Blueprint("home", __name__)

HOMEPAGE_STANDINGS_COLUMNS = [
    {"key": "wins", "label": "W"},
    {"key": "losses", "label": "L"},
    {"key": "pct", "label": "Pct"},
    {"key": "gb", "label": "GB"},
    {"key": "l10", "label": "L10"},
    {"key": "diff", "label": "Diff"},
]


@home_blueprint.route("/")
@home_blueprint.route("/home")
@home_blueprint.route("/index")
def index():
    division_standings = get_division_standings()
    news = get_mlb_news()
    leaders = get_stat_leaders()

    return render_template(
        "index.html",
        division_standings=division_standings,
        columns=HOMEPAGE_STANDINGS_COLUMNS,
        news=news,
        leaders=leaders,
    )
