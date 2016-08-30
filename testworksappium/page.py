from abc import abstractmethod
import logging
import re


from . import class_string, class_repr
from element import Element


log = logging.getLogger(__name__)


class Page(object):

    def __init__(self, appium_driver):
        self.appium_driver = appium_driver
        self.page_source = None
        self.elements = []

    @abstractmethod
    def verify(self):
        """ This method will assert that we have arrived on the expected page. """
        return

    @abstractmethod
    def validate(self):
        """ This method asserts that the page has the correct elements and/or data. """
        return

    def create_page_element(self, locator_key, locator):
        element = Element(self.appium_driver, locator_key, locator)
        self.elements.append(element)
        return element

    def page_contains(self, value):
        does_contain_text = False
        text_regex = re.compile(re.escape(value))
        contains_text = text_regex.search(self.appium_driver.page_source)
        if contains_text:
            does_contain_text = True
        return does_contain_text

    def __str__(self):
        return class_string(self)

    def __repr__(self):
        return class_repr(self)
