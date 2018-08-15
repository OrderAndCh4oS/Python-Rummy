# coding=utf-8
import sys

import pkg_resources

TEMPLATE_PATH = pkg_resources.resource_filename('rummy', 'templates/')
UNICODE_SUPPORT = sys.stdout.encoding.lower().startswith('utf')
VALUES = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
SUITS = ("♠", "♥", "♦", "♣")
ALPHA_SUITS = ("S", "H", "D", "C")
