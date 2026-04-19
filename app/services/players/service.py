from .fetch import fetch_player_data
from .parse import parse_player


def get_player_data(player_id):
    player_data_raw = fetch_player_data(player_id, "career,projected,yearByYear")

    return parse_player(player_data_raw)
