# Testworks Conf Mobile Automation Workshop
## Instructions and Information

Welcome to the Testworks Conf Mobile Automation!

### Useful Tips and Information

#### Links

- [Workshop Github Repo](https://github.com/apallin/testworks-appium)
- [Appium Python Client](https://github.com/appium/python-client)
- [Appium Documentation](http://appium.io/slate/en/master/?ruby#running-appium-tests)
- [Page Object Model Description](http://www.guru99.com/page-object-model-pom-page-factory-in-selenium-ultimate-guide.html)
- [Examples](https://github.com/apallin/testworks-appium/tree/master/examples)

#### Information

- Every Appium boot, or every test, will reset the state of your application.  Do not rely on data from other tests to do operations in another test.
- While functionally testing the application is great, remember that verifying operations you do is crucial.  If you make an event, how would you validate it was created properly?  Be sure to think about these types of scenarios as you develop.
- Page Object's are your friend, [read up](http://www.guru99.com/page-object-model-pom-page-factory-in-selenium-ultimate-guide.html) or search for more information if you are looking for best practices.

### Workshop Goals

At this workshop, we feel it will be possible for you to complete several tasks in the time given.  We have set you up for success, but left you free to explore and learn what you will.  The following is a general progression that has been laid out to help you get the most of this session.

1. Be able to run the “example_test.py” script to ensure you have everything set up and can continue with the workshop.  This will be run by the following commands from the root of the [project](https://github.com/apallin/testworks-appium) directory:
	
	```
	python setup.py install
	APP=demo-app.apk ./run-tests examples/example-test.py
	```
	
2. Once this test runs as expected, move on to create a test for adding a new calendar event.  This will require you to create the following:

	- A folder at the root of the project called `tests/` or something else for you to hold your pages/tests that are created during this workshop.
	- Page objects for the application (check the [demo page](https://github.com/apallin/testworks-appium/blob/master/examples/example_page.py) for an example on how to create them)
		- The main calendar page (first page on app open).
		- The add event page (the page after clicking the + button).
	
	- A "scroll" method to the Page object base class.  In the [appium-python-client](https://github.com/appium/python-client/blob/master/appium/webdriver/webdriver.py#L156) you can see that it takes two elements to use for scrolling.  This will be needed in the add event page to fill in the rest of the details.
	
3. After that test is completed, you can create a test for creating/deleting a calendar event.  Remember, Appium boots the application into a new session with no saved data, so you would need to create a new event to delete in another test.  This would require the following:

	- Page objects for:
		- Day page (once you click into an single day from the main calendar screen).
		- Edit event screen (once you click into an event).
		
	- A new test either in the file already created or in a new file.
	
4.  The next logical test to write would be one for editing an event.  You should be able to leverage everything you have written already and just write a new test to edit the details.

5. If you get through all these tests, think of more scenarios and plug away!  I would suggest the following:

	- Test extra pages like the "Settings" or "About" screens in the menu.
	- Test changing months using the `</>` buttons on the main page.
	- Add extra validation steps to your tests. If you edit an event functionally, are you actually validating the result has changed in the application?

6. If you get through these, the final step would be to make your code more and more concise.  One thing that we leverage greatly is what are called **workflows**.  This is a script of one or more Page objects that do an action.  For example, you could write a workflow for creating a calendar event.  Find some ways to make your code more re-usable.
	
	

		