# coding=utf-8

def green(text):
    return "\033[0;32m" + text + "\033[0m"


def blue(text):
    return "\033[0;36m" + text + "\033[0m"


def grey(text):
    return "\033[0;37m" + text + "\033[0m"

def red(text):
    return "\033[0;31m" + text + "\033[0m"
