# coding=utf-8
from random import shuffle

from rummy.deck.card import Card
from rummy.deck.sort import Sort


class TestSort:

    def test_sort_hand_by_suit_and_rank(self):
        sort = Sort()
        values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
        suits = ("♠", "♥", "♦", "♣")
        hand = [
            Card(values[0], suits[0]),
            Card(values[1], suits[1]),
            Card(values[2], suits[1]),
            Card(values[11], suits[1]),
            Card(values[2], suits[2]),
            Card(values[7], suits[2]),
            Card(values[10], suits[3]),
            Card(values[12], suits[3])
        ]
        hand_copy = hand[:]
        shuffle(sort.sort_hand_by_suit_and_rank(hand_copy))
        assert hand == sort.sort_hand_by_suit_and_rank(hand_copy)

    def test_sort_hand_by_rank(self):
        sort = Sort()
        values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
        suits = ("♠", "♥", "♦", "♣")
        hand = [
            Card(values[0], suits[0]),
            Card(values[1], suits[1]),
            Card(values[2], suits[1]),
            Card(values[2], suits[2]),
            Card(values[7], suits[2]),
            Card(values[10], suits[3]),
            Card(values[11], suits[1]),
            Card(values[12], suits[3])
        ]
        hand_copy = hand[:]
        shuffle(sort.sort_hand_by_rank(hand_copy))
        assert hand == sort.sort_hand_by_rank(hand_copy)
