from flask import Blueprint, render_template

from .services.mlb_news import get_mlb_news
from .services.standings import get_division_standings

home_blueprint = Blueprint("home", __name__)


@home_blueprint.route("/")
@home_blueprint.route("/home")
@home_blueprint.route("/index")
def index():
    division_standings = get_division_standings()
    news = get_mlb_news()

    return render_template(
        "index.html", division_standings=division_standings, news=news
    )
