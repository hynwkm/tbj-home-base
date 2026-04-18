from flask import Blueprint, render_template

teams_blueprint = Blueprint("teams", __name__)


@teams_blueprint.route("/teams/<int:team_id>")
def team(team_id):
    return render_template("team.html", team_id=team_id)
