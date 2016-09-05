#!/usr/bin/env python
import logging
import xml.dom.minidom

from appium import webdriver

log = logging.getLogger(__name__)


class AppiumDriver(webdriver.Remote):
    """
    AppiumDriver class
    Extension of webdriver class
    :param: :webdriver_url: String url for webdriver connection
    :param: :capabilities: Dict of desired capabilities of test
    """

    def __init__(self, webdriver_url=None, capabilities=None):
        self.webdriver_url = webdriver_url
        self.capabilities = capabilities
        log.debug("Connecting to Appium with: {}".format(capabilities))
        super(AppiumDriver, self).__init__(
            self.webdriver_url, self.capabilities)

    def page_source(self):
        """
        Pretty print of page_souce xml object
        :return: formatted xml string
        """
        log.debug("Collecting page source")
        element_source = super(AppiumDriver, self).page_source
        element_utf = element_source.encode('ascii', 'ignore').strip()
        xml_object = xml.dom.minidom.parseString(element_utf)
        return xml_object.toprettyxml('   ')
