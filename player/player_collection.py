from game.setup_players import SetupPlayers
from view.colour import blue


class PlayerCollection(SetupPlayers):
    players = []

    def __init__(self):
        super().__init__()

    def getPlayers(self):
        return self.players
