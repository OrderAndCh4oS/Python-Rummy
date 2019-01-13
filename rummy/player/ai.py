# -*- coding: utf-8 -*-

from rummy.player.player import Player


class AI(Player):

    def __init__(self, num, ai_only=False):
        super().__init__(num)
        self.ai_only = ai_only
