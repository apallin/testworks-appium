import logging
import xml.dom.minidom

from appium import webdriver

log = logging.getLogger(__name__)


class AppiumDriver(webdriver.Remote):

    def __init__(self, capabilities=None):
        self.capabilities = capabilities
        self.port = self.capabilities['port'] if 'port' in self.capabilities else 4723
        self.webdriver_url = 'http://localhost:{}/wd/hub'.format(self.port)

        super(AppiumDriver, self).__init__(self.webdriver_url, self.capabilities)

    def page_source(self):
        log.debug("{} getting page_source")
        element_source = super(AppiumDriver, self).page_source
        element_utf = element_source.encode('ascii', 'ignore').strip()
        xml_object = xml.dom.minidom.parseString(element_utf)
        return xml_object.toprettyxml("   ")

    def set_location(self, location):
        if self.running_on_simulator():
            self.log.debug("{} Setting location to:{}".format(self, location))
            super(AppiumDriver, self).set_location(latitude=location[0], longitude=location[1], altitude=0)
        else:
            self.log.debug("{} Not running on simulator... skipping setting of appium_driver location".format(self))

    def execute(self, driver_command, params=None):
        self.log.debug('{} Sending request: {}, {}'.format(self, driver_command, params))
        result = super(AppiumDriver, self).execute(driver_command, params)
        self.log.debug('{} Finished request: {}, {}'.format(self, driver_command, params))
        return result

    def __str__(self):
        return 'AppiumDriver:{}'.format(self.id)

    def __repr__(self):
        repr_string = 'AppiumDriver Fields: '
        attributes = vars(self)
        repr_string += ''.join('{}: {} '.format(key, value) for (key, value) in attributes.items())
        return repr_string
