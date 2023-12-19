from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EXC

from page_objects.SysProfile import SysProfile


class SysConfig:
    default_config: "default_config_locator"
    memo_req: "memo_req_locator"
    menu: (By.NAME, "Menu")
    profile: ("Profile")

    def __init__(self, driver):
        self.driver = driver
        self.WebDriverWait = WebDriverWait(self.driver, 10)

    def select_default(self):
        self.WebDriverWait.until(EXC.presence_of_element_located((By.CSS_SELECTOR, self.default_config)))
        return self.driver.find_element(By.CSS_SELECTOR, self.default_config).click()

    def require_memo(self):
        self.WebDriverWait.until(EXC.presence_of_element_located((By.XPATH, self.memo_req)))
        return self.driver.find_element(By.XPATH, self.memo_req).click()

    def click_profile(self):
        # open system menu
        self.driver.find_element(*SysConfig.menu).click()
        self.WebDriverWait.until(EXC.presence_of_element_located((By.NAME, self.profile)))
        # navigate to system profile page
        self.driver.find_element(By.NAME, self.profile).click()
        # initialize driver for new page
        profile = SysProfile(self.driver)
        return profile


