# coding=utf-8

from rummy.player.ai import AI
from rummy.player.hand import Hand
from rummy.deck.card import Card
from rummy.deck.deck import Deck
from rummy.game.melds import Melds


class TestAI:
    # This test suite leaves out functions that primarily serve to render templates/text

    def test_choose_to_discard_or_pick_up(self, mocker):
        mocker.patch('builtins.print')
        mocker.spy(AI, 'choose_pick_up')
        mocker.spy(Hand, 'draw_card')
        ai = AI(1)
        ai.round = mocker.MagicMock()
        ai.round.deck.take_card.return_value = Card("A", "♥")
        ai.round.deck.has_discard.return_value = True
        ai.choose_to_discard_or_pick_up()
        assert AI.choose_pick_up.call_count == 1
        assert Hand.draw_card.call_count == 1
        ai.round.deck.has_discard.return_value = False
        ai.choose_to_discard_or_pick_up()
        assert AI.choose_pick_up.call_count == 1
        assert Hand.draw_card.call_count == 2

    def test_choose_pick_up(self, mocker):
        mocker.patch('builtins.print')
        mocker.patch.object(Hand, 'get_score', return_value=45)
        mocker.patch.object(Hand, 'draw_card')
        mocker.patch.object(Melds, 'find_discard_scores', side_effect=[[50, 60, 30], [12, 9, 15], [70]])
        ai = AI(1)
        ai.round = mocker.MagicMock()
        ai.round.deck.take_discard.return_value = Card("A", "♥")
        ai.round.deck.take_card.return_value = Card("2", "♥")
        # Test for min(scores) < current score, but > 10
        ai.choose_pick_up()
        assert ai.round.deck.take_discard.call_count == 1
        assert ai.round.deck.take_card.call_count == 0
        assert ai.hand.draw_card.call_count == 1
        # Test for min(scores) < current_score - 4 and <=10
        ai.choose_pick_up()
        assert ai.round.deck.take_discard.call_count == 2
        assert ai.round.deck.take_card.call_count == 0
        assert ai.hand.draw_card.call_count == 2
        # Test for min(scores) >= current_score - 4 and > 10
        ai.choose_pick_up()
        assert ai.round.deck.take_discard.call_count == 2
        assert ai.round.deck.take_card.call_count == 1
        assert ai.hand.draw_card.call_count == 3

    def test_discard_or_knock(self, mocker):
        mocker.patch('builtins.print')
        # Mock random.choice to assure that the last item from our array of scores is chosen,
        # to make this test predictable/consistent
        mocker.patch('random.choice', side_effect=(2, 8))
        mocker.patch.object(Melds, 'find_discard_scores', side_effect=[[10, 8, 8], [11]])
        mocker.patch.object(Hand, 'discard_card')
        mocker.patch.object(Deck, 'discard_card')
        ai = AI(1)
        ai.round = mocker.MagicMock()
        ai.hand.hand = [Card("A", "♥"), Card("2", "♥")]
        ai.round.knocked = False
        ai.discard_or_knock()
        assert ai.round.knocked
        ai.hand.discard_card.assert_called_with(2)
        assert ai.round.deck.discard_card.call_count == 1
        ai.discard_or_knock()
        assert ai.round.knocked
        ai.hand.discard_card.assert_called_with(0)
        assert ai.round.deck.discard_card.call_count == 2


