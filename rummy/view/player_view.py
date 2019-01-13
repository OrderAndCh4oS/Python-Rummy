from abc import abstractmethod

from text_template import TextTemplate

from rummy.constants.resource_path import TEMPLATE_PATH


class PlayerView:

    @staticmethod
    @abstractmethod
    def turn_start(player):
        pass

    @staticmethod
    @abstractmethod
    def turn_end(player):
        pass

    @staticmethod
    @abstractmethod
    def discarded(discard):
        pass

    @staticmethod
    def knocked():
        return TextTemplate.render(
            TEMPLATE_PATH + '/knocked.txt'
        )
