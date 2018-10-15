# coding=utf-8

from rummy.player.dealer import Dealer
from rummy.deck.deck import Deck


class TestDealer:

    def test_card_count(self):
        dealer = Dealer()
        dealer.set_card_count(7)
        assert Dealer.cardCount == 7

    def test_deal(self):
        dealer = Dealer()
        deck = Deck()
        assert len(dealer.deal(deck.get_deck()).hand) == dealer.cardCount


