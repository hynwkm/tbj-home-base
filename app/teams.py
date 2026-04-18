from flask import Blueprint, render_template

from .services.mlb_news import get_team_news
from .services.standings import get_team_standing_info

teams_blueprint = Blueprint("teams", __name__)


@teams_blueprint.route("/teams/<int:team_id>")
def team(team_id):

    team_info = get_team_standing_info(team_id)

    return render_template("team.html", team_info=team_info)
