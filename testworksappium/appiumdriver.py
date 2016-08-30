import logging
import xml.dom.minidom

from . import class_string, class_repr

from appium import webdriver

log = logging.getLogger(__name__)


class AppiumDriver(webdriver.Remote):

    def __init__(self, webdriver_url=None, capabilities=None):
        super(AppiumDriver, self).__init__(self.webdriver_url, self.capabilities)

    def page_source(self):
        element_source = super(AppiumDriver, self).page_source
        element_utf = element_source.encode('ascii', 'ignore').strip()
        xml_object = xml.dom.minidom.parseString(element_utf)
        return xml_object.toprettyxml('   ')

    def execute(self, driver_command, params=None):
        log.debug('{} Sending request: {}, {}'.format(self, driver_command, params))
        result = super(AppiumDriver, self).execute(driver_command, params)
        log.debug('{} Finished request: {}, {}'.format(self, driver_command, params))
        return result

    def __str__(self):
        return class_string(self)

    def __repr__(self):
        return class_repr(self)
