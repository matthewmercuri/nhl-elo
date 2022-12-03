HOME_ADVANTAGE_ADJUSTMENT: float = 0.05
BACK_TO_BACK_ADVANTAGE_ADJUSTMENT: float = 0.1
K: int = 24


def get_b2b_advantage(home_b2b: bool, away_b2b: bool) -> str | None:
    if home_b2b and not away_b2b:
        return "away"

    if away_b2b and not home_b2b:
        return "home"

    return None


def get_win_probabilities(
    home_team_elo: float, away_team_elo: float, home_b2b: bool, away_b2b: bool
) -> tuple[float, float]:
    home_win_probability = (
        1 / (1 + (10 ** ((away_team_elo - home_team_elo) / 400)))
    ) + HOME_ADVANTAGE_ADJUSTMENT
    away_win_probability = 1 - home_win_probability

    # adjusting for b2b advatage
    b2b_advantage = get_b2b_advantage(home_b2b, away_b2b)

    if b2b_advantage == "home":
        home_win_probability += BACK_TO_BACK_ADVANTAGE_ADJUSTMENT
        away_win_probability = 1 - home_win_probability

    if b2b_advantage == "away":
        away_win_probability += BACK_TO_BACK_ADVANTAGE_ADJUSTMENT
        home_win_probability = 1 - away_win_probability

    return home_win_probability, away_win_probability


def get_updated_elos(
    prev_home_team_elo: float,
    prev_away_team_elo: float,
    home_win_probability: float,
    is_home_win: bool,
):
    if is_home_win:
        home_win = 1
    else:
        home_win = 0

    home_elo_change = K * (home_win - home_win_probability)
    updated_home_elo = prev_home_team_elo + home_elo_change
    updated_away_elo = prev_away_team_elo - home_elo_change

    return updated_home_elo, updated_away_elo
