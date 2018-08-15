# coding=utf-8
from constants.constants import VALUES


class FaceValues:

    @staticmethod
    def get() -> tuple:
        return VALUES

    @staticmethod
    def is_value_in_range(value):
        return value in VALUES
