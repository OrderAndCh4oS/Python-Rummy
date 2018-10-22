# coding=utf-8

from rummy.deck.card import Card
from rummy.game.melds import Melds
from rummy.player.hand import Hand
from rummy.player.human import Human
from rummy.ui.user_input import UserInput


class TestHuman:

    def test_draw_from_deck_or_discard_pile(self, mocker):
        mocker.patch.object(Human, '_choose_pick_up')
        mocker.patch.object(Human, 'take_from_deck')
        human = Human(1)
        human.round = mocker.MagicMock()
        human.round.deck.has_discard.return_value = False
        human.draw_from_deck_or_discard_pile()
        assert human._choose_pick_up.call_count == 0
        assert human.take_from_deck.call_count == 1
        human.round.deck.has_discard.return_value = True
        human.draw_from_deck_or_discard_pile()
        assert human._choose_pick_up.call_count == 1
        assert human.take_from_deck.call_count == 1

    def test__choose_pick_up(self, mocker):
        # TODO: Rewrite this test for new action separation
        human = Human(1)
        mocker.patch.object(UserInput, 'create_input', side_effect=['p', 'd'])
        human.round = mocker.MagicMock()
        mocker.patch.object(human.round.deck, 'take_card', return_value=Card("A", "♥"))
        mocker.patch.object(human.round.deck, 'take_discard', return_value=Card("2", "♥"))
        mocker.spy(Hand, 'draw_card')
        # player_choice = 'p'
        human._choose_pick_up()
        # player_choice = 'd'
        human._choose_pick_up()
        assert Hand.draw_card.call_count == 2
        assert human.round.deck.take_card.call_count == 1
        assert human.round.deck.take_discard.call_count == 1

    def test_discard_or_knock(self, mocker):
        # TODO: Rewrite this test for new action separation
        mocker.patch('builtins.print')
        mocker.patch('builtins.input', side_effect=['k', '1', '3', '5', '3', '4'])
        mocker.patch.object(Melds, 'find_discard_scores', side_effect=[[9, 12], [9, 12], [9, 12], [11, 12], [11, 12]])
        mocker.patch.object(Hand, 'discard_card', return_value=Card("A", "♥"))
        mocker.spy(Hand, 'discard_card')
        human = Human(1)
        human.round = mocker.MagicMock()
        # valid score, not knocked; chooses to knock
        # scores = [9, 12], knocked = False, player_choice = 'k' -> '1'
        human.round.knocked = False
        human.discard_or_knock()
        assert human.round.knocked
        assert Hand.discard_card.call_count == 1

        # valid score, not knocked
        # scores = [9, 12], knocked = False, player_choice = '3'
        human.round.knocked = False
        human.discard_or_knock()
        assert not human.round.knocked
        assert Hand.discard_card.call_count == 2

        # valid score, knocked
        # scores = [9, 12], knocked = True, player_choice = '5'
        human.round.knocked = True
        human.discard_or_knock()
        assert human.round.knocked
        assert Hand.discard_card.call_count == 3

        # invalid score, not knocked
        # scores = [11, 12], knocked = False, player_choice = '3'
        human.round.knocked = False
        human.discard_or_knock()
        assert not human.round.knocked
        assert Hand.discard_card.call_count == 4

        # invalid score, knocked
        # scores = [11, 12], knocked = True, player_choice = '4'
        human.round.knocked = True
        human.discard_or_knock()
        assert human.round.knocked
        assert Hand.discard_card.call_count == 5
