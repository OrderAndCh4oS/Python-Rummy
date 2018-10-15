# coding=utf-8

from rummy.game.round import Round
from rummy.deck.deck import Deck
from rummy.player.human import Human


class TestRound:

    def test_prepare_new_round(self):
        round1 = Round([Human(1)])
        round1.turn = 2
        round1.last_turn = 3
        round1.knocked = True
        round1.prepare_new_round()
        assert round1.turn == 1
        assert round1.last_turn == 1
        assert not round1.knocked
        assert isinstance(round1.deck, Deck)

    def test_deal_cards(self, mocker):
        mocker.spy(Round, 'deal')
        human1 = Human(1)
        human2 = Human(2)
        human3 = Human(3)
        round1 = Round([human1, human2, human3])
        round1.deal_cards([human1, human2])
        assert round1.deal.call_count == 2
        round1.deal_cards([human1, human2, human3])
        assert round1.deal.call_count == 5

    def test_prepare_turn(self, mocker):
        mocker.spy(Deck, 'check_stack')
        mocker.spy(Round, 'check_knocked')
        round1 = Round(1)
        round1.prepare_turn()
        assert Deck.check_stack.call_count == 1
        assert Round.check_knocked.call_count == 1

    def test_end_turn(self, mocker):
        mocker.spy(Round, 'switch_current_player')
        round1 = Round([Human(1)])
        turn_before = round1.turn
        round1.end_turn()
        assert round1.turn == (turn_before + 1)

    def test_check_knocked(self):
        round1 = Round([Human(1)])
        round1.check_knocked()
        assert round1.last_turn == 1
        round1.knocked = True
        round1.check_knocked()
        assert round1.last_turn == 2

    def test_switch_current_player(self):
        round1 = Round([Human(1), Human(2)])
        assert round1.current_player == 0
        round1.switch_current_player()
        assert round1.current_player == 1 % 2

    def test_rotate_first_player(self):
        round1 = Round([Human(1), Human(2)])
        assert round1.first_player == 0
        assert round1.current_player == 0
        round1.rotate_first_player()
        assert round1.first_player == 1
        assert round1.current_player == 1 % 2
