# coding=utf-8
import os
from string import Template

from view.colour import Colour


class View(Colour):
    @classmethod
    def render(cls, template, **kwargs):
        if not os.path.isfile(template):
            raise OSError("Template was not found: " + template)
        with open(template, 'r') as content_file:
            content = content_file.read()
            t = Template(content)
            kwargs.update(cls.colours)
            return t.substitute(**kwargs)
