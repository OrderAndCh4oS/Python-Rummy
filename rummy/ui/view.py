# coding=utf-8

from text_template import TextTemplate

from rummy.constants.resource_path import TEMPLATE_PATH


# Todo: Refactor -- These look more like controllers the current controller is more like a service.


class View:

    @staticmethod
    def render(*args, **kwargs):
        # Just a wrapper/abstraction layer for builtins.print
        # Outputs will go through this class, so that if any
        # complete transformations need to be applied,
        # they can be applied in once place.
        print(*args, **kwargs)

    @staticmethod
    def prepare_template(template, **kwargs):
        complete_template = TEMPLATE_PATH + template
        return TextTemplate.render(complete_template, **kwargs)

