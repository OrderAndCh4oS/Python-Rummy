# coding=utf-8


class ActionCollection:

    def __init__(self, *actions):
        self.actions = []
        self.count = 0
        for action in actions:
            self.count += 1
            self.actions.append(action)

    def add_action(self, action):
        self.count += 1
        self.actions.insert(-1, action)

    def add_actions(self, *actions):
        for action in reversed(actions):
            self.count += 1
            self.actions.insert(-1, action)
