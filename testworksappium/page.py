#!/usr/bin/env python
from abc import abstractmethod
import logging
import re


from . import class_string, class_repr
from element import Element


log = logging.getLogger(__name__)


class Page(object):
    """
    Page object implementation for an application page. Provides methods for
    element/page interactions.
    :param: :appium_driver: webdriver object
    """

    def __init__(self, appium_driver):
        self.appium_driver = appium_driver
        self.page_source = None
        self.elements = []

    @abstractmethod
    def verify(self):
        """
        Assert that we have arrived on the expected page.
        """
        return

    @abstractmethod
    def validate(self):
        """
        Asserts that the page has correct elements and/or data.
        """
        return

    def create_page_element(self, locator_key, locator_value):
        """
        Create a page element object given a locator_key/value
        :param: :locator_key: String locator_key
        :param: :locator_value: String locator_value
        :return: Element object
        """
        element = Element(self.appium_driver,
                          locator_key=locator_key, locator_value=locator_value)
        self.elements.append(element)
        return element

    def page_contains(self, value):
        """
        Search page_source string xml for a given substring value
        :param: :value: string value to find in page source
        :return: Boolean
        """
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
