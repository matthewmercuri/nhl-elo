import data
import elo
from constants import BASE_ELO
from services import get_blank_teams_dict, update_teams_dict

"""
TODO:
- use last played dict to implement b2b adjustment
"""

ALLOWED_GAME_TYPES = ["R", "P"]


def process_game(game, team_elo_dict: dict):
    if game["gameType"] not in ALLOWED_GAME_TYPES:
        return game

    home_name = game["homeTeam"]
    away_name = game["awayTeam"]

    prev_home_elo = team_elo_dict[home_name]
    prev_away_elo = team_elo_dict[away_name]

    game["homePreGameElo"] = prev_home_elo
    game["awayPreGameElo"] = prev_away_elo

    home_win_probability, away_win_probability = elo.get_win_probabilities(
        prev_home_elo, prev_away_elo, False, False
    )

    game["homeWinProbability"] = home_win_probability
    game["awayWinProbability"] = away_win_probability

    if game["gameStatus"] == "Final":
        is_home_win: bool = game["homeScore"] > game["awayScore"]

        updated_home_elo, updated_away_elo = elo.get_updated_elos(
            prev_home_elo,
            prev_away_elo,
            home_win_probability,
            is_home_win,
        )

        update_teams_dict(team_elo_dict, home_name, updated_home_elo)
        update_teams_dict(team_elo_dict, away_name, updated_away_elo)

    return game


def run_elo_pipeline():
    team_elo_dict = get_blank_teams_dict(BASE_ELO)
    schedule_df = data.generate_games_df("20212022")

    schedule_df = schedule_df.apply(process_game, axis=1, team_elo_dict=team_elo_dict)

    schedule_df.to_csv("test.csv")


run_elo_pipeline()
