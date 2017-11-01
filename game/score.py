# coding=utf-8
from view.colour import Colour
from view.view import View


class Score:
    def __init__(self, players):
        self.players = players

    def displayThisRoundScore(self):

        print(View.render(
            template='./templates/round-end.txt',
            round_scores=self.getEndOfRoundScores(),
            game_scores=self.getCurrentGameScores()
        ))

    def getCurrentGameScores(self):
        return ''.join(["%s: %s\n" % (p.getName(), p.getScore()) for p in self.players])

    def getEndOfRoundScores(self):
        # ToDo: Dependency inject view or inherit?
        output = ''
        for p in self.players:
            output += View.render(
                template='./templates/hand-score.txt',
                player=p.getName(),
                hand=p.hand.getHand(),
                score=p.hand.getScore()
            )
        return output

    def updatePlayerScores(self):
        for p in self.players:
            p.updateScore()

    def isEndOfGame(self):
        for p in self.players:
            if p.getScore() >= 100:
                return True
        return False

    def endGame(self):
        self.displayThisRoundScore()
        winners = self.findLowestScores()
        if len(winners) == 1:
            print(Colour.green(winners[0].getName() + " is the Winner!!"))
        else:
            print(Colour.green(", ".join([w.getName() for w in winners]) + " are joint winners!"))

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
