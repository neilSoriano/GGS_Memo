import inspect
import logging

import pytest

# if there are any common utilities you think will be used multiple times,
# add to BaseClass since all functions it will be available to the test file


# use useFixtures("setup") to use fixture method from conftest
@pytest.mark.usefixtures("setup")
class BaseClass:
    existing_id = "9876"

    @staticmethod
    def get_logger():
        # inspect.stack() returns the nested list with frame records for the given function(s) and
        # we are specifically getting first list from the nest and fetching the third element from the list
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log', mode='w')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        # log levels are debug -> info -> warning -> error -> critical
        # setting to debug will allow the logger to display all levels when called
        logger.setLevel(logging.DEBUG)
        return logger