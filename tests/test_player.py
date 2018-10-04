# coding=utf-8

from rummy.player.player import Player
from rummy.player.hand import Hand
from rummy.deck.card import Card


class DummyPlayer(Player):
    # Dummies away the abstract methods from Player to allow testing

    def choose_to_discard_or_pick_up(self):
        pass

    def discard_or_knock(self):
        pass


class TestPlayer:

    def test_player_string(self):
        player = DummyPlayer(1)
        assert str(player) == "Player 1"

    def test_get_name(self):
        player = DummyPlayer(1)
        assert player.get_name() == "Player 1"

    def test_update_score(self):
        player = DummyPlayer(1)
        player.hand.draw_card(Card("A", "♠"))
        player.hand.draw_card(Card("A", "♥"))
        player.hand.draw_card(Card("2", "♥"))
        player.hand.draw_card(Card("3", "♥"))
        player.update_score()
        assert player.game_score == 1

    def test_get_hand(self):
        player = DummyPlayer(1)
        assert type(player.get_hand()) is Hand
        assert not player.get_hand().hand

    def test_get_game_score(self):
        player = DummyPlayer(1)
        assert player.get_game_score() == player.game_score

    def test_display_round_score(self):
        player = DummyPlayer(1)
        assert player.display_round_score() == player.hand.score
