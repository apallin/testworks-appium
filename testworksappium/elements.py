#!/usr/bin/env python
import logging

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

log = logging.getLogger(__name__)


class Elements(object):

    def __init__(self, appium_driver, **kwargs):
        """
        Element object for wrapping webdriver element calls.
        Must pass a locator/locator_value in kwargs to find elements.
        :param: :appium_driver: webdriver object
        """
        self.appium_driver = appium_driver
        self.element_objects = []

        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        locator_key, locator_value = next(iter(kwargs.items()))
        self.locator_value = locator_value
        self.locator_key = locator_key
        self.locator = (locator_key, locator_value)

    def find_elements(self):
        """
        Function for finding element objects for appium interaction.
        :return: webdriver element object
        """
        log.debug("Finding {}".format(self.locator))
        try:
            self.element_objects = self.appium_driver.find_elements(
                by=self.locator_key, value=self.locator_value)
        except NoSuchElementException as e:
            log.error(e)
            pass
        except WebDriverException:
            log.error(e)
            pass
        return self.element_objects
