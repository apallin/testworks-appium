import logging
import unittest
import time

import gevent

from exceptions import TimeoutError

log = logging.getLogger(__name__)

DEFAULT_TIMEOUT = 60
DEFAULT_WAIT = 1


class AppiumTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(AppiumTestCase, self).__init__(*args, **kwargs)

    def setUp(self, **kwargs):
        pass

    def tearDown(self, **kwargs):
        pass

    def create_page(self, page):
        pass

    def start_appium(self, desired_capabilities):
        pass

    def get_current_time(self):
        return time.time()

    def wait_until(
            self,
            test_method,
            result=True,
            timeout_seconds=DEFAULT_TIMEOUT,
            seconds_between=DEFAULT_WAIT,
            *args,
            **kwargs):
        log.debug("Waiting for {} to return {} for {} seconds".format(
            test_method.__name__, result, timeout_seconds))
        start = self.get_current_time()

        test_method_result = None
        while True:
            test_method_result = test_method(*args, **kwargs)
            if result is True and test_method_result:
                return True
            elif result == test_method_result:
                return True
            else:
                log.error("Method {} received response: {} expected: {}.".format(
                    test_method.__name__, test_method_result, result))

            if (self.get_current_time() - start) > timeout_seconds:
                break

            gevent.sleep(seconds_between)

        raise TimeoutError("""
                           Failed waiting for {} to return {};
                           final value was {}""".format(
            test_method.__name__, result, test_method_result))
