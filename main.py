import data
from services import get_blank_seeding_dict

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

ALLOWED_GAME_TYPES = ["R"]


def process_game(game):
    print(game)
    return game


def run_elo_pipeline():
    team_elo_dict = get_blank_seeding_dict()
    schedule_df = data.generate_games_df()

    schedule_df.apply(process_game, axis=1)

    return


run_elo_pipeline()
