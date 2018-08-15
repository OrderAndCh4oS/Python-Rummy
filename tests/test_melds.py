# coding=utf-8
from deck.card import Card
from deck.melds import Melds


class TestMelds:

    def test_find_discard_scores(self):
        melds = Melds()
        hand_sets = [
            Card('A', 'S'),
            Card('A', 'H'),
            Card('A', 'D'),
            Card('A', 'C'),
            Card('2', 'S'),
            Card('2', 'H'),
            Card('2', 'D'),
            Card('2', 'C'),
        ]
        hand_runs = [
            Card('A', 'S'),
            Card('2', 'S'),
            Card('3', 'S'),
            Card('4', 'S'),
            Card('5', 'S'),
            Card('6', 'S'),
            Card('7', 'S'),
            Card('8', 'S'),
        ]
        hand_set_and_run = [
            Card('3', 'S'),
            Card('3', 'H'),
            Card('3', 'D'),
            Card('3', 'C'),
            Card('5', 'S'),
            Card('6', 'S'),
            Card('7', 'S'),
            Card('8', 'S'),
        ]
        hand_crossover = [
            Card('3', 'S'),
            Card('3', 'H'),
            Card('3', 'D'),
            Card('A', 'C'),
            Card('2', 'C'),
            Card('3', 'C'),
            Card('4', 'C'),
            Card('5', 'C'),
        ]
        hand_none = [
            Card('3', 'S'),
            Card('5', 'H'),
            Card('8', 'D'),
            Card('K', 'C'),
            Card('Q', 'S'),
            Card('3', 'H'),
            Card('4', 'D'),
            Card('5', 'C'),
        ]
        assert [0, 0, 0, 0, 0, 0, 0, 0] == melds.find_discard_scores(hand_sets)
        assert [0, 1, 3, 0, 0, 15, 8, 0] == melds.find_discard_scores(hand_runs)
        assert [0, 0, 0, 0, 0, 20, 19, 0] == melds.find_discard_scores(hand_set_and_run)
        assert [6, 6, 6, 0, 1, 12, 5, 0] == melds.find_discard_scores(hand_crossover)
        assert [50, 48, 45, 40, 41, 50, 49, 48] == melds.find_discard_scores(hand_none)

    def test_calculate_score(self):
        melds = Melds()
        hand_sets = [
            Card('A', 'D'),
            Card('A', 'C'),
            Card('A', 'S'),
            Card('2', 'C'),
            Card('2', 'S'),
            Card('2', 'H'),
            Card('2', 'D'),
        ]
        hand_runs = [
            Card('A', 'S'),
            Card('2', 'S'),
            Card('3', 'S'),
            Card('4', 'S'),
            Card('9', 'C'),
            Card('T', 'C'),
            Card('J', 'C'),
        ]
        hand_set_and_run = [
            Card('3', 'S'),
            Card('3', 'H'),
            Card('3', 'D'),
            Card('5', 'S'),
            Card('6', 'S'),
            Card('7', 'S'),
            Card('8', 'S'),
        ]
        hand_crossover = [
            Card('3', 'S'),
            Card('3', 'H'),
            Card('3', 'D'),
            Card('A', 'C'),
            Card('2', 'C'),
            Card('3', 'C'),
            Card('4', 'C'),
        ]
        hand_none = [
            Card('3', 'S'),
            Card('5', 'H'),
            Card('8', 'D'),
            Card('K', 'C'),
            Card('Q', 'S'),
            Card('3', 'H'),
            Card('4', 'D'),
        ]

        assert 0 == melds.calculate_score(hand_sets)
        assert 0 == melds.calculate_score(hand_runs)
        assert 0 == melds.calculate_score(hand_set_and_run)
        assert 0 == melds.calculate_score(hand_crossover)
        assert 48 == melds.calculate_score(hand_none)
