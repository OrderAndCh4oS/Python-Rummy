# coding=utf-8
import re

from rummy.deck.card import Card
from rummy.deck.deck import Deck


class TestDeck:

    def test_deck(self):
        deck = Deck()
        assert 52 == len(deck.get_deck()) and 0 == len(deck.get_discard_pile())

    def test_draw_all_cards(self):
        deck = Deck()
        for _ in range(52):
            deck.discard_card(deck.take_card())
        assert 0 == len(deck.get_deck()) and 52 == len(deck.get_discard_pile())

    def test_check_stack(self):
        deck = Deck()
        for _ in range(52):
            deck.discard_card(deck.take_card())
        deck.check_stack()
        assert 52 == len(deck.get_deck()) and 0 == len(deck.get_discard_pile())

    def test_show_discard(self):
        deck = Deck()
        deck.discard_card(deck.take_card())
        assert re.match(r'[ATJQK2-9].*?[♥♣♦♠]', deck.show_discard())

    def test_has_discard(self):
        deck = Deck()
        deck.discard_card(deck.take_card())
        assert deck.has_discard()

    def test_take_card(self):
        deck = Deck()
        card = deck.take_card()
        assert isinstance(card, Card)
        assert len(deck.get_deck()) == 51

    def test_take_discard(self):
        deck = Deck()
        deck.discard_card(deck.take_card())
        discard = deck.take_discard()
        assert isinstance(discard, Card)
        assert len(deck.get_discard_pile()) == 0

    def test_discard_card(self):
        deck = Deck()
        deck.discard_card(deck.take_card())
        assert len(deck.get_discard_pile()) == 1

    def test_inspect_discard(self):
        deck = Deck()

        deck.discard_card(deck.take_card())
        assert isinstance(deck.inspect_discard(), Card)
        assert len(deck.get_discard_pile()) == 1
