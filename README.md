# Testworks-appium
---
Repository for [Testworks Conf '16](http://testworksconf.com/) Mobile Automation Workshop

Developed by Adam Pallin for the Mobile Automation workshop on Academy Day, October 6th 2016.

## Setup
---

To install just the [module](https://github.com/apallin/testworks-appium/tree/master/testworksappium), download and install from PyPi using:

```
pip install testworksappium
```

If you would like to run the demo test cases, please clone the respository, install using `python setup.py install` and then run the demo tests using:

```
APP=demo-app.apk ./run-tests examples/example-test.py
```

The demo app is compiled from [Simple-Calendar](https://github.com/SimpleMobileTools/Simple-Calendar) and can be cloned, altered if needed.

## Usage
---

### Testcase

The [AppiumTestCase](https://github.com/apallin/testworks-appium/blob/master/testworksappium/testcase.py), built on Python's unittest framework, can be extended and then used to run Appium tests.  See the [example test case](https://github.com/apallin/testworks-appium/blob/master/examples/example_test.py) for usage.

There are two main functions for use during tests:

* [`create_page()`](https://github.com/apallin/testworks-appium/blob/master/testworksappium/testcase.py#L102) is used to create a new Page object during testing.
* [`wait_until()`](https://github.com/apallin/testworks-appium/blob/master/testworksappium/testcase.py#L156) is the main test method that is used to assert certain test methods enter an expected state.
	*  Example:
	   ```
	   self.wait_until(example_page.verify)
	   ```

### Page Object

Test cases get built on [Page objects](https://github.com/apallin/testworks-appium/blob/master/testworksappium/page.py) which are used to organize test code and be a single source of truth for what you Application should look like.  See the [example page](https://github.com/apallin/testworks-appium/blob/master/examples/example_page.py) for usage.

### Element/Elements

Page objects can create and [Element](https://github.com/apallin/testworks-appium/blob/master/testworksappium/element.py) objects or get multiple [Elements](https://github.com/apallin/testworks-appium/blob/master/testworksappium/elements.py).  These elements are the building blocks for interacting with Appium and your app.  They contain functions that can be called by your Page objects or testcases to drive the UI.  Functions like `is_visible()` and `tap()` are core to how users percieve an application and therefore are crucial to your UI testing.

## Test Artifacts
---

When using `AppiumTestCase` all test artifacts get archived in your current working directory under the `test-artifacts` folder created during the run. Each tests data will be archived under a subfolder like `test_name_<test start time>`
This data includes:

* `test.log`: A log file of all python logging calls made during the test.  This is useful for debugging test steps.
* `appium.log`: The Appium application log for the given test.
* `failure_screenshot.jpg`: If the test fails, the testcase takes a screenshot for debugging help.
* `page_tree.xml`:  If the test fails, the testcase archives the xml page source of the application for debugging help.




