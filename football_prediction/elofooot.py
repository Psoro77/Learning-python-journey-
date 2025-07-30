from collections import defaultdict

# Initialiser ELO pour chaque équipe
elo = defaultdict(lambda: 1300)
class EloRating:
    def __init__(self, base_score=1300, k_factor=80):
        self.elo = defaultdict(lambda: base_score)
        self.k = k_factor

    def expected_score(self, rating_a, rating_b):
        return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))

    def update_ratings(self, home_team, away_team, result):
        elo_home = self.elo[home_team]
        elo_away = self.elo[away_team]

        expected_home = self.expected_score(elo_home, elo_away)
        expected_away = 1 - expected_home

        if result == "H":
            score_home, score_away = 1, 0
        elif result == "A":
            score_home, score_away = 0, 1
        elif result == "D":
            score_home = score_away = 0.5
        else:
            return elo_home, elo_away  # match non joué ou FTR vide

        # Update ratings
        new_elo_home = elo_home + self.k * (score_home - expected_home)
        new_elo_away = elo_away + self.k * (score_away - expected_away)

        self.elo[home_team] = new_elo_home
        self.elo[away_team] = new_elo_away

        return new_elo_home, new_elo_away

    def get_rating(self, team):
        return self.elo[team]