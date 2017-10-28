# coding=utf-8

try:
    print(u"\u2660", u"\u2665", u"\u2666", u"\u2663")
    hasUnicode = True
except UnicodeEncodeError:
    hasUnicode = False
