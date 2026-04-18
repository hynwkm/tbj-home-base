from flask import Blueprint, render_template

leaderboard_blueprint = Blueprint("leaderboard", __name__)


@leaderboard_blueprint.route("/leaderboard")
def leaderboards():
    return render_template("leaderboard.html")
