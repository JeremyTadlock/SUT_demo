class ScoreBoard:
    def __init__(self, player_name, winningGoal):
        self.player_name = player_name
        self.human_score = 0
        self.ai_score = 0
        self.winningGoal = winningGoal

    def getScorePlayer(self):
        return self.human_score

    def getScoreAi(self):
        return self.ai_score

    def addScorePlayer(self, amt):
        self.human_score += amt

    def addScoreAi(self, amt):
        self.ai_score += amt