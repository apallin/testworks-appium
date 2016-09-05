#!/usr/bin/env python
from abc import abstractmethod
import logging
import re

from element import Element
from elements import Elements


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

    @abstractmethod
    def verify(self):
        """
        Assert that we have arrived on the expected page.
        """
        return

    def create_element(self, **kwargs):
        """
        Create a page element object given a locator_key/value
        :param: :locator_key: String locator_key
        :param: :locator_value: String locator_value
        :return: Element object
        """
        log.debug("Creating element with {}".format(kwargs))
        element = Element(self.appium_driver, **kwargs)
        return element

    def create_elements(self, **kwargs):
        """
        Create a page element object given a locator_key/value
        :param: :locator_key: String locator_key
        :param: :locator_value: String locator_value
        :return: Element object
        """
        log.debug("Creating elements with {}".format(kwargs))
        elements = Elements(self.appium_driver, **kwargs)
        return elements

    def page_contains(self, value):
        """
        Search page_source string xml for a given substring value
        :param: :value: string value to find in page source
        :return: Boolean
        """
        log.debug("Check if page contains {}".format(value))
        does_contain_text = False
        text_regex = re.compile(re.escape(value))
        contains_text = text_regex.search(self.appium_driver.page_source())
        if contains_text:
            does_contain_text = True
        return does_contain_text
