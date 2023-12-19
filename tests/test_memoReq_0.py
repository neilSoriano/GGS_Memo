import pytest

from page_objects.SysConfig import SysConfig
from page_objects.SysProfile import SysProfile
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("bag_ids")
class TestMemoReq0(BaseClass):

    def test_memo0(self, bag_ids):
        log = self.get_logger()
        log.info("Testing scenario of submitting a memo with 0 characters")

        conf = SysConfig(self.driver)
        log.info("Setting yes to require memo")
        conf.require_memo()

        log.info("Navigating to profile orders page")
        profile = conf.click_profile()
        profile.click_orders()

        log.info("Editing Bag ID to new value")
        new_id = profile.set_bag_id(bag_ids)

        log.info("Not entering any text into memo field; 0 characters")

        account_id = profile.get_profile_glory_id()
        log.info("Checking if profile glory ID is equal to memo glory ID")
        assert profile.get_memo_glory_id() in account_id

        log.info("Date and time is " + profile.get_date_time())

        log.info("Submitting new Bag ID and no memo")
        profile.click_submit()

        log.error("Submit memo of size 0 FAILED")

        # log.info("Confirming Bag ID value has changed")
        # current_id = profile.get_bag_id()
        # assert current_id == new_id








