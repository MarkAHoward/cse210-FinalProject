

class Score:
    def __init__(self):
        self.score = 0

    def score_get(self):
        return self.score

    def score_add(self, points):
        self.score += points
