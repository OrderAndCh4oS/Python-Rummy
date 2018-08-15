from deck.suits import Suits


def test_suits():
    suits = Suits()
    assert ("♠", "♥", "♦", "♣") == suits.get()
