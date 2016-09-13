from testworksappium import Page


class CreateEventPage(Page):

    def __init__(self, appium_driver):
        super(CreateEventPage, self).__init__(appium_driver)
        self.event_title_field = self.create_element(
            id='com.simplemobiletools.calendar:id/event_holder')

    def verify(self):
        return self.event_title_field.is_displayed()

    def validate(self):
        assert self.page_contains("Title")
        assert self.page_contains("Description")

    def add_title(self, title):
        self.event_title_field.send_keys(title)
