from flask import Flask


def create_app():
    app = Flask(__name__)

    from .home import home_blueprint
    from .leaderboard import leaderboard_blueprint
    from .players import players_blueprint
    from .standings import standings_blueprint
    from .teams import teams_blueprint

    app.register_blueprint(home_blueprint)
    app.register_blueprint(standings_blueprint)
    app.register_blueprint(teams_blueprint)
    app.register_blueprint(players_blueprint)
    app.register_blueprint(leaderboard_blueprint)

    return app
