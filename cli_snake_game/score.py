## score.py
class Score:
    def __init__(self):
        self.score = 0

    def increment(self):
        self.score += 1

    def get_score(self):
        return self.score
