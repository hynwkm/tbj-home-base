from .fetch import fetch_player_data, fetch_player_game_logs
from .parse import parse_game_log_stats, parse_player


def get_player_data(player_id):
    player_data_raw = fetch_player_data(player_id, "career,projected,yearByYear")

    return parse_player(player_data_raw)


def get_player_game_logs(player_id: int):
    position, stat_splits = fetch_player_game_logs(player_id)

    return parse_game_log_stats(position, stat_splits)
