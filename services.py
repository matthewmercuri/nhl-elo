import data

BASE_ELO = 1200


def get_blank_seeding_dict() -> dict:
    teams_list = data.get_teams_list()
    seed_dict = dict(zip(teams_list, [BASE_ELO] * len(teams_list)))

    return seed_dict


def update_elo_dict(elo_dict: dict, team_name: str, updated_elo: float) -> dict:
    elo_dict.update({team_name: updated_elo})

    return elo_dict
