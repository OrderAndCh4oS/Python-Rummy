# coding=utf-8
import os
from string import Template


class View:
    def render(self, template, **kwargs):
        if not os.path.isfile(template):
            raise OSError("Template was not found")
        with open(template, 'r') as content_file:
            content = content_file.read()
            t = Template(content)
            return t.substitute(**kwargs)
