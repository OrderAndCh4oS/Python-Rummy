from deck.suits import Suits


class TestSuits:

    def test_suits(self):
        assert ("♠", "♥", "♦", "♣") == Suits.get()

    def test_alpha_to_unicode_suit_glyph(self):
        assert "♠" == Suits.alpha_to_unicode_suit_glyph('S')
        assert "♥" == Suits.alpha_to_unicode_suit_glyph('H')
        assert "♦" == Suits.alpha_to_unicode_suit_glyph('D')
        assert "♣" == Suits.alpha_to_unicode_suit_glyph('C')
