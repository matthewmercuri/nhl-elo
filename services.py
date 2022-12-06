import data
from typing import Any


def get_blank_teams_dict(initial_value) -> dict:
    teams_list = data.get_teams_list()
    return dict(zip(teams_list, [initial_value] * len(teams_list)))


def update_teams_dict(elo_dict: dict, team_name: str, updated_value: Any) -> dict:
    elo_dict.update({team_name: updated_value})
    return elo_dict


def update_last_played_dict(
    last_played_dict: dict, team_name: str, game_date: str
) -> dict:
    last_played_dict.update({team_name: game_date})
    return last_played_dict
