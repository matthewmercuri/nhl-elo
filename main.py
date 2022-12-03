import data
import elo
from services import get_blank_seeding_dict, update_elo_dict

"""
run_elo_pipeline pseudo code
1. get elo seeding dict
2. iterate through schedule
    a. reference elo dict for team elos
    b. compute new elos/win probabilities
    c. update schedule df
    d. update elo_dict states
3. return schedule df
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
        is_home_win = game["homeScore"] > game["awayScore"]

        updated_home_elo, updated_away_elo = elo.get_updated_elos(
            prev_home_elo,
            prev_away_elo,
            home_win_probability,
            is_home_win,
        )

        update_elo_dict(team_elo_dict, home_name, updated_home_elo)
        update_elo_dict(team_elo_dict, away_name, updated_away_elo)

    return game


def run_elo_pipeline():
    team_elo_dict = get_blank_seeding_dict()
    schedule_df = data.generate_games_df("20212022")

    schedule_df.apply(process_game, axis=1, args=(team_elo_dict))

    return


run_elo_pipeline()
