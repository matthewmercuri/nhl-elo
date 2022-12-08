import numpy as np
import pandas as pd
from .nhlApi import get_seasons_games, get_team_names


def generate_games_df(season_string: str) -> pd.DataFrame:
    seasons_games_list = get_seasons_games(season_string)
    df = pd.DataFrame(seasons_games_list)

    # INFO:
    # - may be able to just reassign to gameDate column
    # - pythonGameDate seems to be the same as pandasGameDate
    df["pandasGameDate"] = pd.to_datetime(df["gameDate"], infer_datetime_format=True)
    df["pythonGameDate"] = df["pandasGameDate"].dt.to_pydatetime()

    df.sort_values(by="pandasGameDate", ascending=True, inplace=True)
    df.reset_index(inplace=True, drop=True)

    df["homePreGameElo"] = 0
    df["awayPreGameElo"] = 0

    df["isHomeB2B"] = np.nan
    df["isAwayB2B"] = np.nan

    df["homeWinProbability"] = 0
    df["awayWinProbability"] = 0

    return df


def get_teams_list() -> list:
    return get_team_names()
