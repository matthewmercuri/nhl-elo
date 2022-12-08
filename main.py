import data
import elo
from constants import BASE_ELO, ALLOWED_GAME_TYPES
from services import get_blank_teams_dict, update_teams_dict, has_played_yesterday


def process_game(game, team_elo_dict: dict, last_played_dict: dict):
    if game["gameType"] not in ALLOWED_GAME_TYPES:
        return game

    home_name = game["homeTeam"]
    away_name = game["awayTeam"]

    prev_home_elo = team_elo_dict[home_name]
    prev_away_elo = team_elo_dict[away_name]

    game["homePreGameElo"] = prev_home_elo
    game["awayPreGameElo"] = prev_away_elo

    game_date = game["pandasGameDate"]
    is_home_b2b = has_played_yesterday(last_played_dict, home_name, game_date)
    is_away_b2b = has_played_yesterday(last_played_dict, away_name, game_date)
    game["isHomeB2B"] = is_home_b2b
    game["isAwayB2B"] = is_away_b2b

    home_win_probability, away_win_probability = elo.get_win_probabilities(
        prev_home_elo, prev_away_elo, is_home_b2b, is_away_b2b
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

        update_teams_dict(last_played_dict, home_name, game_date)
        update_teams_dict(last_played_dict, away_name, game_date)

    return game


def run_elo_pipeline():
    team_elo_dict = get_blank_teams_dict(BASE_ELO)
    last_played_dict = get_blank_teams_dict(None)

    schedule_df = data.generate_games_df("20212022")

    schedule_df = schedule_df.apply(
        process_game,
        axis=1,
        team_elo_dict=team_elo_dict,
        last_played_dict=last_played_dict,
    )

    schedule_df.to_csv("test.csv")


run_elo_pipeline()
