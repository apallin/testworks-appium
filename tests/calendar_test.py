#!/usr/bin/env python
from testworksappium import AppiumTestCase
from main_page import MainPage
from create_event_page import CreateEventPage


class CalendarAppTests(AppiumTestCase):

    def test_example(self):
        main_page = self.create_page(MainPage)
        self.wait_until(main_page.verify)
        self.main_page.validate()

    def test_create_event(self):
        # Validate main page
        main_page = self.create_page(MainPage)
        self.wait_until(main_page.verify)
        main_page.validate()
        # Open create event page
        main_page.tap_create_event_button()
        # Validate create event page
        create_event_page = self.create_page(CreateEventPage)
        self.wait_until(create_event_page.verify)
        create_event_page.validate()
        # Add title
        create_event_page.add_title("Test Title")
        # Add description
        # Set start time
        # Set end time
        # Create event
