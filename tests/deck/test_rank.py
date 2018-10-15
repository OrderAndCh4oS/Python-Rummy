# coding=utf-8
from rummy.deck.card import Card
from rummy.deck.rank import Rank


class TestRank:

    def test_rank(self):
        rank = Rank()
        values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
        suits = (u"♠", u"♥", u"♦", u"♣")
        assert rank.ranked_cards == [Card(value, suit) for suit in suits for value in values]

    def test_get_suit_and_rank_key_ace_of_spades(self):
        rank = Rank()
        assert (0, 0) == rank.get_suit_and_rank_key(Card('A', '♠'))

    def test_get_suit_and_rank_key_king_of_clubs(self):
        rank = Rank()
        assert (3, 12) == rank.get_suit_and_rank_key(Card('K', '♣'))

    def test_get_suit_and_rank_key_seven_of_diamonds(self):
        rank = Rank()
        assert (2, 6) == rank.get_suit_and_rank_key(Card('7', '♦'))

    def test_get_rank_key_seven(self):
        rank = Rank()
        assert 6 == rank.get_rank_key(Card('7', '♦'))

    def test_get_rank_key_ace(self):
        rank = Rank()
        assert 0 == rank.get_rank_key(Card('A', '♦'))

    def test_get_rank_key_ten(self):
        rank = Rank()
        assert 9 == rank.get_rank_key(Card('T', '♦'))
