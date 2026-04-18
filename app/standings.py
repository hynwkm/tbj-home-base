from flask import Blueprint, render_template

from .services.standings import get_division_standings

standings_blueprint = Blueprint("standings", __name__)


@standings_blueprint.route("/standings")
def standings():
    division_standings = get_division_standings()
    return render_template("standings.html", division_standings=division_standings)
