

class Card:
    value = ""
    suit = ""

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def getCardColour(self):
        if self.suit in [u"\u2665", u"\u2666", "H", "D"]:
            return self.redCard()
        elif self.suit in [u"\u2660", u"\u2663", "C", "S"]:
            return self.blackCard()

    def redCard(self):
        # if hasUnicode:
        #     return str(self.value) + "\033[1;31m" + self.suit + "\033[0m, "
        # else:
        #     return str(self.value) + self.suit + ", "
        return str(self.value) + "\033[1;31m" + self.suit + "\033[0m, "

    def blackCard(self):
        return str(self.value) + self.suit + ", "