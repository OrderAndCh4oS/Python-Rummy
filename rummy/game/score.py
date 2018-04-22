# coding=utf-8
from ansi_colours import AnsiColours as Colour
from text_template import TextTemplate as View
from ..constants.package_resource_path import TEMPLATE_PATH


class Score:
    def __init__(self, players):
        self.players = players

    def displayThisRoundScore(self):
        print(View.render(
            template=TEMPLATE_PATH + '/round-end.txt',
            round_scores=self.getEndOfRoundScores(),
            game_scores=self.getCurrentGameScores()
        ))

    def getCurrentGameScores(self):
        return ''.join(["%s: %s\n" % (p.getName(), p.getScore()) for p in self.players])

    def getEndOfRoundScores(self):
        output = ''
        for p in self.players:
            output += View.render(
                template=TEMPLATE_PATH + '/hand-score.txt',
                player=p.getName(),
                hand=p.hand.getHand(),
                score=p.hand.getScore()
            )
        return output

    def updatePlayerScores(self):
        for p in self.players:
            p.hand.calculateScore()
            p.updateScore()

    def isEndOfGame(self):
        for p in self.players:
            if p.getScore() >= 100:
                return True
        return False

    def endGame(self):
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
