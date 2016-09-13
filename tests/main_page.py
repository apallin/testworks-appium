from testworksappium import Page


class MainPage(Page):

    def __init__(self, appium_driver):
        super(MainPage, self).__init__(appium_driver)
        self.create_event_button = self.create_element(
            id='calendar_fab')
        self.forward_month_button = self.create_element(
            id="com.simplemobiletools.calendar:id/top_right_arrow")
        self.backward_month_button = self.create_element(
            id="com.simplemobiletools.calendar:id/top_left_arrow")
        self.calendar_view = self.create_element(
            id="com.simplemobiletools.calendar:id/calendar_coordinator")

    def verify(self):
        return self.create_event_button.is_displayed()

    def validate(self):
        assert self.page_contains("Calendar")
        assert self.forward_month_button.is_displayed()
        assert self.backward_month_button.is_displayed()
        assert self.calendar_view.is_displayed()

    def tap_create_event_button(self):
        self.create_event_button.tap()
