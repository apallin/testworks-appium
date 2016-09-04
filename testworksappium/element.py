#!/usr/bin/env python
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

from . import class_string, class_repr
from exceptions import ElementObjectNotSet

log = logging.getLogger(__name__)

_LOCATOR_MAP = {
    'id_': MobileBy.ID,
    'xpath': MobileBy.XPATH,
    'tag_name': MobileBy.TAG_NAME,
    'class_name': MobileBy.CLASS_NAME,
    'android': MobileBy.ANDROID_UIAUTOMATOR,
}


class Element(object):

    def __init__(self, appium_driver, **kwargs):
        """
        Element object for wrapping webdriver element calls.
        Must pass a locator/locator_value in kwargs to find elements.
        :param: :appium_driver: webdriver object
        """
        self.appium_driver = appium_driver
        self.action = TouchAction(self.appium_driver)
        self.element_object = None

        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        locator_key, locator_value = next(iter(kwargs.items()))
        self.locator_value = locator_value
        self.locator_key = locator_key
        self.locator = (_LOCATOR_MAP[locator_key], locator_value)

    def find_element(self):
        """
        Function for finding element object for appium interaction.
        :return: webdriver element object
        """
        try:
            self.element_object = self.appium_driver.find_element(
                by=self.locator_key, value=self.locator_value)
        except NoSuchElementException:
            pass
        except WebDriverException:
            pass
        return self.element_object

    def is_visible(self):
        """
        Check for if element is visible
        :return: Boolean
        """
        self.find_element()
        return [self.element_object.is_visible()
                if self.element_object else False]

    def is_present(self):
        """
        Check for if element is present.
        :return: Boolean
        """
        self.find_element()
        return [self.element_object.is_present()
                if self.element_object else False]

    def is_enabled(self):
        """
        Check for if element is enabled
        :return: Boolean
        """
        self.find_element()
        return [self.element_object.is_enabled()
                if self.element_object else False]

    def tap(self, x=0, y=0, count=1):
        """
        Tap element object if element has already been found
        Example:
        self.element.find_element().tap()
        :param: :x: int offset x for tap
        :param: :y: int offset y for tap
        :param: :count: int number of times to tap
        """
        if self.element_object:
            return self.action.tap(
                self.element_object, x=x, y=y, count=count).perform()

        raise ElementObjectNotSet

    def set_value(self, text):
        """
        Set value of element to provided string if element
        has been found.
        Example:
        self.element.find_element().set_value("foo")
        :param: :text: string to set element
        """
        if self.element_object:
            return self.element_object.set_value(text)

        raise ElementObjectNotSet

    def send_keys(self, keys):
        """
        Send keys to element if element has been found.
        Example:
        self.element.find_element().send_keys("foo")
        :param: :keys: string of keys to send.
        """
        if self.element_object:
            return self.element_object.send_keys(keys)

        raise ElementObjectNotSet

    def text(self):
        """
        Get text of an element object.
        Example:
        self.element.find_element().text()
        """
        if self.element_object:
            return self.element_object.text

        raise ElementObjectNotSet

    def __str__(self):
        return class_string(self)

    def __repr__(self):
        return class_repr(self)
