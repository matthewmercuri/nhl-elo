import pandas as pd
from .nhlApi import get_seasons_games, get_team_names


def create_games_df() -> pd.DataFrame:
    seasons_games_list = get_seasons_games()
    return pd.DataFrame(seasons_games_list)


def create_teams_df():
    print(get_team_names())
