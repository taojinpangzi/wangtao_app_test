import time
from page.home_page import *


class TestEnterPaymentPage:
    def setup_class(self):
        self.home_page = HomePage()

    @staticmethod
    def teardown_class():
        DriverTools.quit_driver()

    def test01(self):
        time.sleep(3)
        self.home_page.tap_mine_button()

    def test02(self):
        time.sleep(3)
        self.home_page.click_login_button()

    def test03(self):
        print(self.home_page.find_el((By.XPATH, "//*[contains(@text,'不能为空')]")).text)

