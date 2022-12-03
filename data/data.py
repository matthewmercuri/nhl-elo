import pandas as pd
from .nhlApi import get_seasons_games, get_team_names


CURRENT_SEASON_STR: str = "20222023"


def generate_games_df(season: str = CURRENT_SEASON_STR) -> pd.DataFrame:
    seasons_games_list = get_seasons_games(season)
    df = pd.DataFrame(seasons_games_list)

    df["awayPreGameElo"] = 0
    df["homePreGameElo"] = 0

    return df


def get_teams_list() -> list:
    return get_team_names()
