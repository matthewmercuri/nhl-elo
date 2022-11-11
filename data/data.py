import pandas as pd
from .nhlApi import get_seasons_games


def create_games_df() -> pd.DataFrame:
    seasons_games_list = get_seasons_games()
    return pd.DataFrame(seasons_games_list)
