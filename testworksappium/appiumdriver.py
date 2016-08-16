import logging
import xml.dom.minidom

from . import class_string, class_repr

from appium import webdriver

log = logging.getLogger(__name__)


class AppiumDriver(webdriver.Remote):

    def __init__(self, webdriver_url=None, capabilities=None):
        super(AppiumDriver, self).__init__(self.webdriver_url, self.capabilities)

    def page_source(self):
        log.debug('{} getting page_source')
        element_source = super(AppiumDriver, self).page_source
        element_utf = element_source.encode('ascii', 'ignore').strip()
        xml_object = xml.dom.minidom.parseString(element_utf)
        return xml_object.toprettyxml('   ')

    def set_location(self, location):
        if self.running_on_simulator():
            self.log.debug('{} Setting location to:{}'.format(self, location))
            super(AppiumDriver, self).set_location(latitude=location[0], longitude=location[1], altitude=0)
        else:
            self.log.debug('{} Not running on simulator... skipping setting of appium_driver location'.format(self))

    def execute(self, driver_command, params=None):
        self.log.debug('{} Sending request: {}, {}'.format(self, driver_command, params))
        result = super(AppiumDriver, self).execute(driver_command, params)
        self.log.debug('{} Finished request: {}, {}'.format(self, driver_command, params))
        return result

    def __str__(self):
        return class_string(self)

    def __repr__(self):
        return class_repr(self)
