# -*- coding: utf-8 -*-

from random import shuffle

from rummy.deck.rank import Rank


class Deck(Rank):
    deck = []
    discard_pile = []

    def __init__(self):
        super().__init__()
        self.deck = self.ranked_cards[:]
        self.discard_pile = []
        shuffle(self.deck)

    def check_stack(self):
        if len(self.deck) == 0:
            self.deck = self.discard_pile
            self.discard_pile = []

    def show_discard(self):
        return self.discard_pile[-1].get_card_colour() if len(self.discard_pile) else 'Empty'

    def get_deck(self):
        return self.deck

    def get_discard_pile(self):
        return self.discard_pile

    def has_discard(self):
        return len(self.discard_pile) > 0

    def take_card(self):
        return self.deck.pop()

    def take_discard(self):
        return self.discard_pile.pop()

    def inspect_discard(self):
        return self.discard_pile[-1]

    def discard_card(self, card):
        return self.discard_pile.append(card)
