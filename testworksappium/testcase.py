#!/usr/bin/env python
import logging
import os
import signal
from subprocess import Popen, PIPE
import sys
import time
import unittest

from appiumdriver import AppiumDriver
from exceptions import TimeoutError


log = logging.getLogger(__name__)

# DEFAULT CONFIGS
DEFAULT_TIMEOUT = 60
DEFAULT_WAIT = 1
DEFAULT_PLATFORM = "Android"
DEFAULT_PLATFORM_VERSION = "6.0"
DEFAULT_DEVICE_NAME = "Android Emulator"
TEST_ARTIFACTS_DIR = "{}/test-artifacts".format(os.getcwd())
# LOGGER CONFIGS
LOG_FORMAT = "[%(asctime)s] %(levelname)s " + \
    " [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
DATE_FORMAT = "%H:%M:%S"
LEVEL = "DEBUG"


class AppiumTestCase(unittest.TestCase):
    """
    Demo appium test case for Testworks Conf workshop.
    Must create a new test case in the ../tests folder.
    """

    def __init__(self, *args, **kwargs):
        super(AppiumTestCase, self).__init__(*args, **kwargs)
        self.appium_driver = None
        self.appium_proc = None

    def setUp(self, **kwargs):
        log.debug("Starting {}".format(self.__name__))
        test_start_time = self.get_current_time()
        # Make test run directory
        self.test_output_dir = os.path.join(TEST_ARTIFACTS_DIR,
                                            "{}_{}".format(
                                                self.__name__,
                                                test_start_time))
        if not os.path.exists(self.test_output_dir):
            os.makedirs(self.test_output_dir)
        # Set up test logger
        if log.root.handlers:
            log.root.handlers = []
        logging.basicConfig(
            filename="{}/test.log".format(self.test_output_dir),
            level=LEVEL, format=LOG_FORMAT, datefmt=DATE_FORMAT)
        # Stop/Start Appium Server
        self.stop_appium_server()
        self.start_appium_server()
        # Parse Capabilities
        self.app = os.getenv("APP")
        if not self.app:
            raise Exception("No test application set with export APP=")
        desired_capabilities = {
            "noSign": True,
            "app": self.app,
            "platformName": DEFAULT_PLATFORM,
            "platformVersion": DEFAULT_PLATFORM_VERSION,
            "deviceName": DEFAULT_DEVICE_NAME
        }

        # Connect to appium driver
        self.connect_to_appium(desired_capabilities)

    def tearDown(self, **kwargs):
        log.debug("Tearing down {}".format(self.__name__))
        sys_exc_info = sys.exc_info()
        test_passed = sys_exc_info == (None, None, None)

        # Check if tests passed and take final screenshot/page source if failed
        if not test_passed and self.appium_driver:
            log.error(
                "Failed! {}".format(sys_exc_info[1]))
            screenshot_filename = os.path.join(self.test_output_dir,
                                               "failure_screenshot.jpeg")
            self.appium_driver.save_screenshot(screenshot_filename)
            page_tree_file_name = os.path.join(self.test_output_dir,
                                               "page_tree.xml")
            with open(page_tree_file_name, 'w') as page_tree_file:
                element_tree = self.appium_driver.page_source()
                for line in element_tree:
                    page_tree_file.write(element_tree)

        # Quit appium driver
        if self.appium_driver:
            self.appium_driver.quit()

        # Stop appium server
        self.stop_appium_server()
        log.debug("{0} END {0}".format("=" * 25))

    def create_page(self, page_object):
        """
        Method for taking a page object and adding the appium_driver for the
        current test case to it for ease of instantiation.
        :param: :page_object: Page object to create
        :param: :validate: Boolean to validate page as part of creation
        """
        created_page = page_object(self.appium_driver)
        created_page.testcase = self
        return created_page

    def connect_to_appium(self, capabilities):
        """
        Open tests connection to appium driver on local host.
        :param: :capabilities: Dict of test capabilities.
        """
        webdriver_url = "http://localhost:4723/wd/hub"
        self.appium_driver = AppiumDriver(
            webdriver_url=webdriver_url,
            capabilities=capabilities)

    def start_appium_server(self):
        """
        Start appium server on localhost.
        """
        log.debug("Starting Appium Server")
        cmd = "appium --log {}/appium.log".format(self.test_output_dir)
        self.appium_proc = Popen(
            cmd, stdout=PIPE, shell=True, preexec_fn=os.setsid)
        # Need a hard sleep to wait for appium to start
        time.sleep(5)

    def stop_appium_server(self):
        """
        Stop appium server on localhost.
        """
        if self.appium_proc:
            log.debug("Stopping Appium: {}".format(self.appium_proc.pid))
            os.killpg(os.getpgid(self.appium_proc.pid), signal.SIGTERM)
        else:
            p = Popen(['ps', '-A'], stdout=PIPE)
            out, err = p.communicate()
            for process in out.splitlines():
                if 'appium' in process:
                    pid = int(process.split(None, 1)[0])
                    log.debug("Stopping Appium: {}".format(pid))
                    os.kill(pid, signal.SIGKILL)

    def get_current_time(self):
        """
        Return current time stamp.
        """
        return int(time.time())

    def wait_until(
            self,
            test_method,
            result=True,
            timeout_seconds=DEFAULT_TIMEOUT,
            seconds_between=DEFAULT_WAIT,
            *args,
            **kwargs):
        """
        Test method for asserting/retrying for a function to return expected
        condition.
        Examples:
        Wait till element is visible
        self.wait_until(self.element.is_visible())
        Wait till element is not visible
        self.wait_until(self.element.is_visible(), result=False)
        """
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
                log.error("Method {} received response: {}\n"
                          "expected: {}.".format(
                              test_method.__name__,
                              test_method_result,
                              result))

            if (self.get_current_time() - start) > timeout_seconds:
                break

            time.sleep(seconds_between)

        raise TimeoutError("Failed waiting for {} to return {};\n"
                           "final value was {}".format(
                               test_method.__name__,
                               result, test_method_result))
