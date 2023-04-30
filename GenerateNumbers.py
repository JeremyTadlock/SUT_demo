import random


class GenerateNumbers:
    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.player_number = self.setNumbers()
        self.ai_number = self.setNumbers()

    # generate random nunmbers
    def setNumbers(self):
        number = random.randint(self.min, self.max)
        return number

    # get random number
    def getPlayerNumber(self):
        return self.player_number

    def getAiNumber(self):
        return self.ai_number
