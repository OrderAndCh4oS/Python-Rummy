# coding=utf-8
import re

from ansi_colours import AnsiColours as Colour
from rummy.player.hand import Hand
from rummy.player.dealer import Dealer
from rummy.deck.deck import Deck
from rummy.deck.card import Card


class TestHand:

    def test_hand(self):
        hand = Hand()
        assert hand.score == 0

    def test_hand_string(self):
        hand = Dealer().deal(Deck().deck)
        assert len(re.findall(r'[ATJQK2-9].*?[♥♣♦♠]', str(hand))) == 7

    def test_set_hand(self):
        hand1 = Hand()
        hand1.hand = [Card(x, y) for x, y in [("A", "♥"), ("2", "♥"), ("3", "♥"), ("T", "♥"), ("J", "♥"), ("Q", "♥")]]
        hand2 = Hand()
        hand2.set_hand(hand1.hand)
        assert hand1.hand == hand2.hand

    def test_draw_card(self):
        hand = Hand()
        hand.draw_card(Card("A", "♥"))
        assert re.match(r'A.*?♥', str(hand))

    def test_discard_card(self):
        hand = Dealer().deal(Deck().deck)
        hand.discard_card(0)
        assert len(hand.hand) == 6

    def test_get_score(self):
        hand = Hand()
        hand.hand = [Card(x, y) for x, y in [("7", "♠"), ("7", "♥"), ("8", "♦")]]
        assert isinstance(hand.get_score(), int)
        assert hand.get_score() == 22

    def test_get_key(self):
        test_hand = Hand()
        test_hand.hand = [Card(x, y) for x, y in [("A", "♥"), ("2", "♥"), ("3", "♥"), ("4", "♥"),
                                                  ("T", "♥"), ("J", "♥"), ("Q", "♥")]]
        key_string = ',  '.join(["%s" % Colour.green(str((i + 1))) for i in range(7)])
        assert test_hand.get_key() == key_string
