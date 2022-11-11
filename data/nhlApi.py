import requests

"""
Utilizing unofficial publicly documented API, available at:
https://gitlab.com/dword4/nhlapi
"""

BASE_NHL_API_URL: str = "https://statsapi.web.nhl.com/api/v1/"
SCHDULE_API_URL: str = BASE_NHL_API_URL + "schedule"
CURRENT_SEASON_STR: str = "20222023"


def _clean_daily_game_data_list(daily_game_data_list: list[dict]) -> list[dict]:
    return daily_game_data_list


def get_regular_season_games() -> list[dict]:
    params = {"season": CURRENT_SEASON_STR}
    r = requests.get(SCHDULE_API_URL, params)
    daily_game_data_list: list[dict] = r.json()["dates"]

    return _clean_daily_game_data_list(daily_game_data_list)


get_regular_season_games()
