
class PlayerActions:

    @staticmethod
    def take_from_deck(hand, deck):
        hand.draw_card(deck.take_card())

    @staticmethod
    def take_from_discard(hand, deck):
        hand.draw_card(deck.take_discard())

    @staticmethod
    def discard(user_input, hand, deck):
        user_input = int(user_input) - 1
        deck.discard_card(hand.discard_card(user_input))

    @staticmethod
    def knock(round):
        round.knocked = True

