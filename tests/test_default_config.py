import pytest

from page_objects.SysConfig import SysConfig
from page_objects.SysProfile import SysProfile
from utilities.BaseClass import BaseClass


@pytest.usefixtures("bag_ids")
class TestNoMemo(BaseClass):
    def test_same_id(self):
        log = self.get_logger()
        log.info("Testing scenario of not requiring a memo and keeping the Bag ID the same")

        conf = SysConfig(self.driver)
        log.info("Disabling memo requirement")
        conf.select_default()

        log.info("Navigating to profile orders page")
        profile = conf.click_profile()
        profile.click_orders()

        log.info("Clicking submit without changing the Bag ID")
        profile.click_submit()

        log.error("Submit disabled due to no change in Bag ID FAIL")

    def test_new_id(self, bag_ids):
        log = self.get_logger()
        log.info("Testing scenario of not requiring a memo and changing the Bag ID")

        # Based off the first test, we should already be on this page when this test file runs
        # still need to initialize a driver
        profile = SysProfile(self.driver)

        log.info("Editing Bag ID to new value")
        new_id = profile.set_bag_id(bag_ids)

        log.info("Submitting new Bag ID")
        profile.click_submit()

        log.info("Confirming Bag ID value has changed")
        current_id = profile.get_bag_id()
        assert current_id == new_id
