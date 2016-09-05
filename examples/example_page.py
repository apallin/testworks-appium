from testworksappium import Page


class ExamplePage(Page):

    def __init__(self, appium_driver):
        super(ExamplePage, self).__init__(appium_driver)
        self.example_element = self.create_element(
            id='calendar_fab')

    def verify(self):
        return self.example_element.is_displayed()

    def tap_example_element(self):
        self.example_element.tap()
