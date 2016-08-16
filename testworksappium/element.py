import logging

from clientautomation.appium.exceptions import ElementNotFoundException


from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

log = logging.getLogger(__name__)


_LOCATOR_MAP = {
    'id_': MobileBy.ID,
    'xpath': MobileBy.XPATH,
    'tag_name': MobileBy.TAG_NAME,
    'class_name': MobileBy.CLASS_NAME,
    'ios': MobileBy.IOS_UIAUTOMATION,
    'android': MobileBy.ANDROID_UIAUTOMATOR,
}


class Element(object):

    def __init__(self, appium_driver=None, **kwargs):
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

    def find_element(self, timeout=None, reset=False):
        log.debug("{} Finding Element".format(self))
        if reset:
            self.element_object = None
        if not self.element_object:
            if timeout:
                self.element_object = WebDriverWait(self.appium_driver, self.timeout).until(
                    EC.visibility_of_element_located((self.locator))
                )
            else:
                self.element_object = self.appium_driver.find_element(by=self.locator)
            log.debug("Found: {}".format(self))
        return self.element_object

    def tap(self, x=None, y=None, count=1):
        """
        Basic tap function implementation for an element.
        :x: x-axis offset for tapping
        :y: y-axis offset for tapping
        :count: number of times to tap
        """
        if self.find_element():
            log.debug("{} Tapping".format(self))
            return self.action.tap(self.element_object, x=x, y=y, count=count).perform()

        raise ElementNotFoundException(self)

    def long_press(self, duration=1000):
        """
        Press function for duration provided.
        :duration: duration in milliseconds to press
        """
        if self.find_element():
            log.debug("{} Pressing with duration={}".format(self, duration))
            return self.action.long_press(self.element_object, None, None, duration).perform()

        raise ElementNotFoundException(self)

    def send_keys(self, text):
        """
        Send key combination to element.  Used for filling in text.
        :text: text to fill in with function
        """
        if self.find_element():
            log.debug("{} Sending keys {}".format(self, text))
            return self.element_object.send_keys(text)

        raise ElementNotFoundException(self)

    def set_value(self, text):
        """
        Set value of element to text.  Similar to send_keys but used for different interaction.
        :text: text to set with function
        """
        if self.find_element():
            log.debug("{} Setting value to {}".format(self, text))
            return self.element_object.set_value(text)

        raise ElementNotFoundException(self)

    def clear(self):
        """
        """
        if self.find_element():
            log.debug("{} Clearing".format(self))
            return self.element_object.clear()

    def text(self):
        """
        Get text of element.
        """
        if self.find_element():
            log.debug("{} Text is {}".format(self, self.element_object.text))
            return self.element_object.text

        raise ElementNotFoundException(self)

    def is_present(self):
        """
        Check if element is present in application.  Basis for all further interatctions.
        """
        is_present = True
        try:
            self.find_element()
        except NoSuchElementException:
            log.debug("{} captured NoSuchElementException, returning False".format(self))
            is_present = False
        except WebDriverException:
            log.debug("{} captured WebDriverException, returning False".format(self))
            is_present = False
        return is_present()

    def is_visible(self):
        """
        Check if element is visible or not.
        """
        return bool(self.find_element())

    def is_enabled(self):
        """
        Check if element is enabled or not.
        """
        if self.is_present():
            log.debug("{} enabled is {}".format(self, self.element_object.is_enabled()))
            return bool(self.element_object.is_enabled())

        return False

    def __str__(self):
        return 'Element {}: Locator: {}'.format(self.__class__.__name__, self.locator)

    def __repr__(self):
        return self.__str__()


class MultiElement(object):

    def __init__(self, appium_driver=None, timeout=MAX_TIMEOUT, **kwargs):
        self.appium_driver = appium_driver
        self.element_objects = []
        self.timeout = timeout
        log = logging.getLogger("MultiElement")
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator{}".format(**kwargs))
        locator_key, locator_value = next(iter(kwargs.items()))
        self.locator_value = locator_value
        self.locator = (_LOCATOR_MAP[locator_key], locator_value)

    def find_all(self):
        try:
            log.debug("Finding all elements for {}".format(self.locator))
            self.element_objects = WebDriverWait(self.appium_driver, self.timeout).until(
                EC.presence_of_all_elements_located((self.locator))
            )
            log.debug("Elements found for {} = {}".format(self.locator, self.element_objects))
            return self.element_objects
        except NoSuchElementException:
            raise ElementNotFoundException(self)
