# coding=utf-8

from rummy.deck.card import Card


class TestCard:

    def test_value_ace(self):
        card = Card("A", "H")
        assert "A" == card.value

    def test_value_number(self):
        card = Card("7", "H")
        assert "7" == card.value

    def test_suit_plain(self):
        card = Card("A", "H")
        assert card.suit == "H"

    def test_red_card_plain_text(self):
        card = Card("A", "H")
        assert 'A\x1b[0;31mH\x1b[0m' == card.get_card_colour()

    def test_diamond_glyph(self):
        card = Card("8", "♦")
        assert '8\x1b[0;31m♦\x1b[0m' == card.get_card_colour()

    def test_heart_glyph(self):
        card = Card("T", "♥")
        assert 'T\x1b[0;31m♥\x1b[0m' == card.get_card_colour()

    def test_club_glyph(self):
        card = Card("K", "♣")
        assert 'K♣' == card.get_card_colour()

    def test_spade_glyph(self):
        card = Card("A", "♠")
        assert 'A♠' == card.get_card_colour()
