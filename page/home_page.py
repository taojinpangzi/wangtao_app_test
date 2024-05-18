from selenium.webdriver.common.by import By

from common.base import *


class HomePage(Base):
    def __init__(self):
        super().__init__()
        self.login_register_button = (By.XPATH, "//*[@text='登录/注册途虎会员']")
        self.login_button = (By.XPATH, "//*[@text='验证并登录']")

    def tap_mine_button(self):
        self.tap_coordinate(x_coordinate=965, y_coordinate=2265)

    def click_login(self):
        self.click_el(self.login_register_button)

    def click_login_button(self):
        self.click_el(self.login_button)


if __name__ == '__main__':
    homepage = HomePage()
    homepage.tap_mine_button()
    homepage.click_login_button()
