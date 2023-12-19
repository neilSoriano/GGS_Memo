import pytest

from page_objects.SysConfig import SysConfig
from page_objects.SysProfile import SysProfile
from utilities.BaseClass import BaseClass


class TestMemoSameID(BaseClass):
    def test_same_id_1(self):
        log = self.get_logger()
        log.info("Testing scenario of submitting a memo without changing the Bag ID")

        conf = SysConfig(self.driver)
        log.info("Setting yes to require memo")
        conf.require_memo()

        log.info("Navigating to profile orders page")
        profile = conf.click_profile()
        profile.click_orders()

        profile.set_memo("keeping bag ID the same")
        log.error("Memo field disabled due to no change in Bag ID FAIL")

    def test_same_id_2(self):
        log = self.get_logger()
        log.info("Testing scenario of submitting a memo, but deleting the Bag ID and retyping it in.")

        # Based off the first test, we should already be on this page when this test file runs
        # still need to initialize a driver
        profile = SysProfile(self.driver)

        log.info("Deleting and reusing the existing Bag ID")
        new_id = profile.set_bag_id(self.existing_id)

        profile.set_memo("Keeping bag ID the same")
        log.error("Memo field disabled due to no change in Bag ID FAIL")





