import logging

from . import class_string, class_repr

log = logging.getLogger(__name__)


class Element(object):

    def __init__(self, appium_driver, **kwargs):
        self.appium_driver = appium_driver
        self.element_object = None

    def is_visible(self):
        pass

    def is_present(self):
        pass

    def is_enabled(self):
        pass

    def tap(self):
        pass

    def long_press(self):
        pass

    def set_value(self):
        pass

    def send_keys(self):
        pass

    def text(self):
        pass

    def __str__(self):
        return class_string(self)

    def __repr__(self):
        return class_repr(self)
