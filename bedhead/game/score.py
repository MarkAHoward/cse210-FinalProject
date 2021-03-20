class Score:
    def __init__(self):
        self.score = 0

    def get_score_text(self):
        score_text = f"Score: {self.score}"
        return score_text

    def add_score(self, points):
        self.score += points
