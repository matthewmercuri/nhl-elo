import data
from datetime import timedelta
from pandas import Timestamp
from typing import Any


def get_blank_teams_dict(initial_value) -> dict:
    teams_list = data.get_teams_list()
    return dict(zip(teams_list, [initial_value] * len(teams_list)))


def update_teams_dict(elo_dict: dict, team_name: str, updated_value: Any) -> dict:
    elo_dict.update({team_name: updated_value})
    return elo_dict


def has_played_yesterday(
    last_played_dict: dict, team_name: str, current_game_date: Timestamp
) -> bool:
    if last_played_dict[team_name] is None:
        return False

    delta: timedelta = current_game_date - last_played_dict[team_name]
    days = delta.days
    hours = delta.seconds / (60 * 60)

    if days < 1 or (days == 1 and hours == 0):
        return True

    return False
