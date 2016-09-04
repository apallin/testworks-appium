#!/usr/bin/env python
class TimeoutError(Exception):

    """
    An exception raised when a test times out waiting for expected condition
    """


class ElementObjectNotSet(Exception):

    """
    An exception to be raised when an element_object has been not set or found
    """
