# coding=utf-8


class FaceValues:
    values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')

    def get(self) -> tuple:
        return self.values

    def is_value_in_range(self, value):
        return value in self.values
