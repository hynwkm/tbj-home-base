from flask import Blueprint, render_template

players_blueprint = Blueprint("players", __name__)


@players_blueprint.route("/players/<int:player_id>")
def player(player_id):
    return render_template("player.html", player_id=player_id)
