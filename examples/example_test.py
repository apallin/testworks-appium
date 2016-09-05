#!/usr/bin/env python
from testworksappium import AppiumTestCase
from example_page import ExamplePage


class TestExample(AppiumTestCase):

    def test_example(self):
        example_page = self.create_page(ExamplePage)
        self.wait_until(example_page.verify)
        assert example_page.page_contains("Calendar")
        example_page.tap_example_element()
