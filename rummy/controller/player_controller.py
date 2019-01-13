from abc import abstractmethod, ABCMeta

from rummy.player.player import Player
from rummy.ui.view import View


class PlayerController(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def show_start_turn(player: Player):
        pass

    @staticmethod
    @abstractmethod
    def show_end_turn(player: Player):
        pass

    @staticmethod
    @abstractmethod
    def show_discard(player: Player):
        pass

    @classmethod
    @abstractmethod
    def draw_card(cls, player):
        pass

    @staticmethod
    @abstractmethod
    def _choose_pick_up(player):
        pass

    @classmethod
    @abstractmethod
    def discard_or_knock(cls, player):
        pass

    @staticmethod
    @abstractmethod
    def _choose_discard(player):
        pass

    @staticmethod
    def show_knocked(player):
        if player.has_someone_knocked():
            View.render(View.prepare_template('/knocked.txt'))
