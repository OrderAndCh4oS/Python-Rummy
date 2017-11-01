# coding=utf-8

class Colour():
    colours = {
        'red': '\033[0;31m',
        'green': '\033[0;32m',
        'blue': '\033[0;36m',
        'grey': '\033[0;37m',
        'colour_end': '\033[0m'
    }

    @classmethod
    def green(cls, text):
        return cls.colours['green'] + text + cls.colours['colour_end']

    @classmethod
    def blue(cls, text):
        return cls.colours['blue'] + text + cls.colours['colour_end']

    @classmethod
    def grey(cls, text):
        return cls.colours['grey'] + text + cls.colours['colour_end']

    @classmethod
    def red(cls, text):
        return cls.colours['red'] + text + cls.colours['colour_end']
