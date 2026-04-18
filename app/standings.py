from flask import Blueprint, render_template

from .services.standings import get_division_standings

standings_blueprint = Blueprint("standings", __name__)


FULL_STANDINGS_COLUMNS = [
    {"key": "wins", "label": "W"},
    {"key": "losses", "label": "L"},
    {"key": "pct", "label": "Pct"},
    {"key": "gb", "label": "GB"},
    {"key": "l10", "label": "L10"},
    {"key": "diff", "label": "Diff"},
    {"key": "home_pct", "label": "Home"},
    {"key": "away_pct", "label": "Away"},
    {"key": "1run_pct", "label": "1-Run"},
    {"key": "xtra_inn_pct", "label": "XInn"},
]


@standings_blueprint.route("/standings")
def standings():
    division_standings = get_division_standings()
    return render_template(
        "standings.html",
        division_standings=division_standings,
        columns=FULL_STANDINGS_COLUMNS,
    )
