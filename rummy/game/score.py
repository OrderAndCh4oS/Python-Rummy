# coding=utf-8
from time import sleep

from ansi_colours import AnsiColours as Colour
from text_template import TextTemplate as View

from rummy.constants.package_resource_path import TEMPLATE_PATH


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
        return ''.join(["%s: %s\n" % (p.getName(), p.getGameScore()) for p in self.players])

    def getEndOfRoundScores(self):
        output = ''
        lessThanTen = False
        for p in self.players:
            score = p.hand.getScore()
            if score <= 10:
                lessThanTen = True
            output += View.render(
                template=TEMPLATE_PATH + '/hand-score.txt',
                player=p.getName(),
                hand=p.hand.getHandToPrint(),
                score=score
            )
        if not lessThanTen:
            print(Colour.red('<+++++++++++++++++++BUG+++++++++++++++++++++++++'))
            sleep(8)
        return output

    def updatePlayerScores(self):
        for p in self.players:
            p.hand.getScore()
            p.updateScore()

    def isEndOfGame(self):
        for p in self.players:
            if p.getGameScore() >= 100:
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
            if p.getGameScore() < lowest[0].getGameScore():
                lowest = [p]
            elif p.getGameScore() == lowest[0].getGameScore():
                lowest.append(p)
        return lowest
