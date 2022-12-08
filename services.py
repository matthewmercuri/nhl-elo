import data
from typing import Any


def get_blank_teams_dict(initial_value) -> dict:
    teams_list = data.get_teams_list()
    return dict(zip(teams_list, [initial_value] * len(teams_list)))


def update_teams_dict(elo_dict: dict, team_name: str, updated_value: Any) -> dict:
    elo_dict.update({team_name: updated_value})
    return elo_dict


# TODO: adjust type of current_game_date
def has_played_yesterday(last_played_dict: dict, current_game_date: Any) -> bool:
    return False
