# coding=utf-8

from rummy.game.setup_players import SetupPlayers


class TestSetupPlayers:

    def test_choose_players(self, mocker):
        mocker.patch('builtins.input', side_effect=[6, 2, 1, 2])
        setup = SetupPlayers()
        # With no AI players, and having given one invalid input, `input` should be called twice
        assert input.call_count == 2
        assert setup.number_of_players == 2
        assert setup.number_of_opponents == -1
        setup.choose_players()
        # After repeating, with a valid but singular number of opponents, `input` has had 4 calls
        # The 4th call comes from inside `choose_number_of_ai_opponents`
        assert input.call_count == 4
        assert setup.number_of_players == 1
        assert setup.number_of_opponents == 2

    def test_setup_ai(self, mocker):
        mocker.patch.object(SetupPlayers, 'choose_players')
        mocker.patch('builtins.input', side_effect=[2, 1])
        mocker.spy(SetupPlayers, 'choose_number_of_ai_opponents')
        setup = SetupPlayers()
        setup.setup_ai(0)
        assert SetupPlayers.choose_number_of_ai_opponents.call_count == 1
        assert setup.number_of_opponents == 2
        setup.setup_ai(1)
        assert SetupPlayers.choose_number_of_ai_opponents.call_count == 2
        assert setup.number_of_opponents == 1

    def test_choose_number_of_ai_opponents(self, mocker):
        mocker.patch.object(SetupPlayers, 'choose_players')
        mocker.patch('builtins.input', side_effect=[4, 1, 6])
        setup = SetupPlayers()
        setup.choose_number_of_ai_opponents(4)
        assert input.call_count == 1
        assert setup.number_of_opponents == 4
        setup.choose_number_of_ai_opponents(3)
        assert input.call_count == 2
        assert setup.number_of_opponents == 1
        setup.choose_number_of_ai_opponents(6)
        assert input.call_count == 3
        assert setup.number_of_opponents == 6

    def test_create_players(self, mocker):
        mocker.patch.object(SetupPlayers, 'choose_players')
        setup = SetupPlayers()
        setup.number_of_players = 2
        setup.number_of_opponents = 2
        assert len(setup.create_players()) == 4

    def test_valid_number_check(self):
        # This method will be moved to a new class, so I'm avoiding testing it here.
        pass
