# coding=utf-8


class Action:
    def __init__(self, key, label):
        self.key = key
        self.label = label

    def __repr__(self):
        return self.label
