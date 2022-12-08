import requests

"""
Utilizing unofficial publicly documented API, available at:
https://gitlab.com/dword4/nhlapi
"""

BASE_NHL_API_URL: str = "https://statsapi.web.nhl.com/api/v1/"
SCHDULE_API_URL: str = BASE_NHL_API_URL + "schedule"
TEAMS_API_URL: str = BASE_NHL_API_URL + "teams"


def _clean_daily_game_data_list(daily_game_data_list: list[dict]) -> list[dict]:
    cleaned_game_data_list: list[dict] = []
    for day_data_dict in daily_game_data_list:
        for game_data in day_data_dict["games"]:
            cleaned_game_data_list.append(
                {
                    "gameType": game_data["gameType"],
                    "season": game_data["season"],
                    "gameDate": game_data["gameDate"],
                    "gameStatus": game_data["status"]["detailedState"],
                    "homeTeam": game_data["teams"]["home"]["team"]["name"],
                    "awayTeam": game_data["teams"]["away"]["team"]["name"],
                    "homeScore": game_data["teams"]["home"]["score"],
                    "awayScore": game_data["teams"]["away"]["score"],
                }
            )

    return cleaned_game_data_list


def get_seasons_games(season_string: str) -> list[dict]:
    params = {"season": season_string}
    r = requests.get(SCHDULE_API_URL, params)
    daily_game_data_list: list[dict] = r.json()["dates"]

    return _clean_daily_game_data_list(daily_game_data_list)


def get_team_names() -> list:
    r = requests.get(TEAMS_API_URL)
    team_data = r.json()["teams"]
    return list(map(lambda team: team["name"], team_data))
