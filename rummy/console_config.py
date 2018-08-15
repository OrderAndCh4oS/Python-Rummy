import os

import colorama


class ConsoleConfig:
    # Todo: move this somewhere else
    @staticmethod
    def colorama():
        if 'PYCHARM_HOSTED' in os.environ:
            convert = False  # in PyCharm, we should disable convert
            strip = False
        else:
            convert = None
            strip = None
        colorama.init(convert=convert, strip=strip)
