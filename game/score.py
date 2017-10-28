# coding=utf-8

from colours.colours import green

class Score:
    def __init__(self, players):
        self.players = players

    def displayThisRoundScore(self):
        for p in self.players:
            p.displayRoundScore()

    def displayCurrentScores(self):
        print("Game Scores")
        for p in self.players:
            print("%s: %s" % (p.getPlayerName(), p.getScore()))

    def updatePlayerScores(self):
        for p in self.players:
            p.updateScore()

    def isEndOfGame(self):
        for p in self.players:
            if p.getScore() >= 100:
                return True
        return False

    def endGame(self):
        winners = self.findLowestScores()
        if len(winners) == 1:
            print(green(winners[0].getPlayerName() + " is the Winner!!"))
        else:
            print(green(", ".join([w.getPlayerName() for w in winners]) + " are joint winners!"))
        self.displayCurrentScores()

    def findLowestScores(self):
        lowest = []
        for p in self.players:
            if not lowest:
                lowest = [p]
                continue
            if p.getScore() < lowest[0].getScore():
                lowest = [p]
            elif p.getScore() == lowest[0].getScore():
                lowest.append(p)
        return lowest
