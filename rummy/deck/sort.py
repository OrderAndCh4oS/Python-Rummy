from rummy.deck.rank import Rank


class Sort:

    def __init__(self):
        self.rank = Rank()

    def sortHandBySuitAndRank(self, cards):
        return sorted(cards, key=lambda card: self.suitAndRankKey(card))

    def sortHandByRank(self, cards):
        return sorted(cards, key=lambda card: self.rankKey(card))

    def suitAndRankKey(self, card):
        return self.rank.suits.index(card.suit), self.rank.values.index(card.value)

    def rankKey(self, card):
        return self.rank.values.index(card.value)
