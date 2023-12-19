import pytest

from page_objects.SysConfig import SysConfig
from page_objects.SysProfile import SysProfile
from utilities.BaseClass import BaseClass


@pytest.usefixtures("bag_ids", "memo_1")
class TestMemoReq1(BaseClass):

    def test_memo1(self, bag_ids, memo_1):
        log = self.get_logger()
        log.info("Testing scenario of submitting a memo with 1 character")

        conf = SysConfig(self.driver)
        log.info("Setting yes to require memo")
        conf.require_memo()

        log.info("Navigating to profile orders page")
        profile = conf.click_profile()
        profile.click_orders()

        log.info("Editing Bag ID to new value")
        new_id = profile.set_bag_id(bag_ids)

        log.info("Adding memo size of 1")
        profile.set_memo(memo_1)

        account_id = profile.get_profile_glory_id()
        log.info("Checking if profile glory ID is equal to memo glory ID")
        assert profile.get_memo_glory_id() in account_id

        log.info("Date and time is " + profile.get_date_time())

        log.info("Submitting new Bag ID with memo")
        profile.click_submit()

        log.info("Confirming Bag ID value has changed")
        current_id = profile.get_bag_id()
        assert current_id == new_id



