import data

BASE_ELO = 1200


def get_blank_seeding_dict():
    teams_list = data.get_teams_list()
    seed_dict = dict(zip(teams_list, [BASE_ELO] * len(teams_list)))

    return seed_dict
