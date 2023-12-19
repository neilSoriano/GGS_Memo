from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EXC


class SysProfile:
    orders_section: "orders"
    bag_id: "Bag ID"
    memo: "Memo"
    memo_glory_id: "memoGloID"
    date_time: "dateTime"
    submit: "Submit"
    profile_glory_id: "gloID"

    def __init__(self, driver):
        self.driver = driver
        self.WebDriverWait = WebDriverWait(self.driver, 10)

    def click_orders(self):
        return self.driver.find_element(By.NAME, self.orders_section).click()

    def get_bag_id(self):
        return self.driver.find_element(By.NAME, self.bag_id).text

    def set_bag_id(self, id):
        self.driver.find_element(By.NAME, self.bag_id).clear()
        self.driver.find_element(By.NAME, self.bag_id).send_keys(id)

    def set_memo(self, text):
        self.driver.find_element(By.NAME, self.memo).clear()
        self.driver.find_element(By.NAME, self.memo).send_keys(text)

    def get_memo_glory_id(self):
        return self.driver.find_element(By.ID, self.memo_glory_id).text

    def get_date_time(self):
        return self.driver.find_element(By.ID, self.date_time).text

    def click_submit(self):
        return self.driver.find_element(By.NAME, self.submit).click()

    # will use to assert against the glory ID captured when memo is entered
    def get_profile_glory_id(self):
        return self.driver.find_element(By.ID, self.profile_glory_id).text



