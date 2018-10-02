# -*- coding: utf-8 -*-

import sys

from rummy.play import Play


def main():
    try:
        Play()
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":
    main()
