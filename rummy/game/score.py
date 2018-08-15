# -*- coding: utf-8 -*-
from time import sleep

from ansi_colours import AnsiColours as Colour
from text_template import TextTemplate as View

from rummy.constants.constants import TEMPLATE_PATH


class Score:
    def __init__(self, players):
        self.players = players

    def display_this_round_score(self):
        print(View.render(
            template=TEMPLATE_PATH + '/round-end.txt',
            round_scores=self.get_end_of_round_scores(),
            game_scores=self.get_current_game_scores()
        ))

    def get_current_game_scores(self):
        return ''.join(["%s: %s\n" % (p, p.get_game_score()) for p in self.players])

    def get_end_of_round_scores(self):
        output = ''
        less_than_ten = False
        for p in self.players:
            score = p.hand.get_score()
            if score <= 10:
                less_than_ten = True
            output += View.render(
                template=TEMPLATE_PATH + '/hand-score.txt',
                player=p.get_name(),
                hand=str(p.hand),
                score=score
            )
        if not less_than_ten:
            print(Colour.red('<+++++++++++++++++++BUG+++++++++++++++++++++++++'))
            sleep(8)
        return output

    def update_player_scores(self):
        for p in self.players:
            p.hand.get_score()
            p.update_score()

    def is_end_of_game(self):
        for p in self.players:
            if p.get_game_score() >= 100:
                return True
        return False

    def end_game(self):
        winners = self.find_lowest_scores()
        if len(winners) == 1:
            print(Colour.green("%s is the Winner!!" % winners[0]))
        else:
            print(Colour.green(", ".join([w for w in winners]) + " are joint winners!"))

    def find_lowest_scores(self):
        lowest = []
        for p in self.players:
            if not lowest:
                lowest = [p]
                continue
            if p.get_game_score() < lowest[0].get_game_score():
                lowest = [p]
            elif p.get_game_score() == lowest[0].get_game_score():
                lowest.append(p)
        return lowest
