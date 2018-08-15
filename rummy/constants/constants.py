# coding=utf-8
import sys

import pkg_resources

TEMPLATE_PATH = pkg_resources.resource_filename('rummy', 'templates/')
UNICODE_SUPPORT = sys.stdout.encoding.lower().startswith('utf')
