# coding=utf-8

from ui.view import View


class Validator:

    @staticmethod
    def valid_number_check(number):
        try:
            number = int(number)
        except ValueError:
            number = -1
            View.render("Not a valid number, please try again...")
        return number
