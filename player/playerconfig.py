from player.hand import Hand


class PlayerConfig:
    def __init__(self, num):
        self.num = num
        self.score = 0
        self.hand = Hand()

    def getPlayerName(self):
        return "Player %i" % self.num

    def updateScore(self):
        self.score += self.hand.score

    def getScore(self):
        return self.score

    def getHand(self):
        return self.hand

    def displayRoundScore(self):
        return self.hand.score