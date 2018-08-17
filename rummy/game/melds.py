# -*- coding: utf-8 -*-

from copy import deepcopy
from itertools import combinations

from rummy.deck.rank import Rank
from rummy.deck.sort import Sort


class Melds:

    def __init__(self):
        self.rank = Rank()
        self.melds = []

    def find_discard_scores(self, hand, discard=None):
        scores = []
        hand_copy = deepcopy(hand)
        if discard is not None:
            hand_copy.append(discard)
        for i in range(len(hand_copy)):
            dummy_hand = deepcopy(hand_copy)
            dummy_hand.pop(i)
            score = self.calculate_score(dummy_hand)
            scores.append(score)
        return scores

    def calculate_score(self, hand):
        self.melds = []
        hand = Sort.sort_hand_by_suit_and_rank(hand)
        cards = {self.rank.get_suit_and_rank_key(card) for card in hand}
        self.find_sets(hand)
        self.find_runs(hand)
        all_possible_melds = self.find_all_possible_melds()
        if len(all_possible_melds) > 0:
            scores = self.find_lowest_scoring_melds(all_possible_melds, cards)
            score = min(scores)
        else:
            score = sum([x[1] + 1 for x in cards])
        return score

    def find_all_possible_melds(self):
        all_possible_melds = []
        for L in range(1, 3):
            for subset in combinations(self.melds, L):
                all_possible_melds.append(subset)
        return all_possible_melds

    def find_lowest_scoring_melds(self, all_possible_melds, cards):
        scores = []
        for item in all_possible_melds:
            if len(item) > 1:
                for i in range(len(item) - 1):
                    if item[i].isdisjoint(item[i + 1]):
                        scores = self.find_scores(item, i, cards, scores)
            else:
                remaining_cards = cards.difference(item[0])
                scores.append(sum([x[1] + 1 for x in remaining_cards]))
        return scores

    def find_scores(self, item, i, cards, scores):
        items = item[i] | item[i + 1]
        remaining_cards = cards.difference(items)
        scores.append(sum([x[1] + 1 for x in remaining_cards]))
        return scores

    def find_sets(self, hand):
        hand = Sort.sort_hand_by_rank(hand)
        cards = [self.rank.get_suit_and_rank_key(card) for card in hand]
        i = 1
        while i < len(cards):
            i, meld = self.make_set_meld(cards, i)
            self.make_all_set_melds(meld)
            i += 1

    def find_runs(self, hand):
        hand = Sort.sort_hand_by_suit_and_rank(hand)
        cards = [self.rank.get_suit_and_rank_key(card) for card in hand]
        i = 1
        while i < len(cards):
            i, meld = self.make_run_meld(cards, i)
            self.make_all_run_melds(meld)
            i += 1

    def make_set_meld(self, cards, i):
        meld = []
        while i < len(cards) and cards[i][1] == cards[i - 1][1]:
            meld.append(cards[i - 1])
            i += 1
        meld.append(cards[i - 1])
        return i, meld

    def make_run_meld(self, cards, i):
        meld = []
        while i < len(cards) and cards[i][0] == cards[i - 1][0] and cards[i][1] == cards[i - 1][1] + 1:
            meld.append(cards[i - 1])
            i += 1
        meld.append(cards[i - 1])
        return i, meld

    def make_all_set_melds(self, meld):
        if len(meld) >= 3:
            self.melds.append(set(meld))
        if len(meld) > 3:
            for width in range(3, len(meld)):
                more_melds = combinations(meld, width)
                for meld in more_melds:
                    self.melds.append(set(meld))

    def make_all_run_melds(self, meld):
        if len(meld) >= 3:
            self.melds.append(set(meld))
        if len(meld) > 3:
            for width in range(3, len(meld)):
                for i, step in enumerate(range(len(meld) - 2)):
                    self.melds.append(set(meld[step:width + i]))


if __name__ == '__main__':
    import sys

    def main():
        from rummy.deck.rank import Rank
        key = [
            'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠',
            '8♠', '9♠', 'T♠', 'J♠', 'Q♠', 'K♠',
            'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥',
            '8♥', '9♥', 'T♥', 'J♥', 'Q♥', 'K♥',
            'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦',
            '8♦', '9♦', 'T♦', 'J♦', 'Q♦', 'K♦',
            'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣',
            '8♣', '9♣', 'T♣', 'J♣', 'Q♣', 'K♣'
        ]
        rank = Rank()
        melds = Melds()
        cards = rank.ranked_cards
        while True:
            handString = input('Hand String: ')
            hand = [cards[key.index(card)] for card in handString.split(', ')]
            if len(hand) > 7:
                scores = melds.find_discard_scores(hand)
                print('Possible Scores: ', scores)
                print('Discard: ', hand.pop(scores.index(min(scores))))
            print('Hand: ', ', '.join([str(card) for card in hand]))
            print('Score: ', melds.calculate_score(hand))
            print("\n==============================\n")

    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
