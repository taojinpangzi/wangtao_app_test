import time
from page.home_page import *


class TestTuHu:
    def setup_class(self):
        self.home_page = HomePage()

    def teardown_class(self):
        time.sleep(5)
        self.home_page.quit_driver()

    def test01(self):
        self.home_page.tap_mine_button()

    def test02(self):
        time.sleep(5)
        self.home_page.click_login()

    def test03(self):
        time.sleep(5)
        self.home_page.click_login_button()

    def test04(self):
        print(self.home_page.explicit_wait_xpath("//*[contains(@text,'不能为空')]").text)

