from flask import Blueprint, render_template

from .services.leaderboard import get_hitter_leaders, get_pitcher_leaders

leaderboard_blueprint = Blueprint("leaderboard", __name__)


@leaderboard_blueprint.route("/leaderboard")
def leaderboards():

    hitters_leaders = get_hitter_leaders()
    pitchers_leaders = get_pitcher_leaders()
    return render_template(
        "leaderboard.html",
        hitters_leaders=hitters_leaders,
        pitchers_leaders=pitchers_leaders,
    )
