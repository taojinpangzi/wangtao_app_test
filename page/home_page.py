import time
from appium.webdriver.common.appiumby import AppiumBy
from common.base import *


class HomePage(Base):
    def __init__(self):
        super().__init__()
        # “我的”按钮
        self.mine_button = (AppiumBy.XPATH, "//android.view.View[@content-desc='我的']")
        # homepage的搜索按钮
        self.home_page_search_button = (AppiumBy.XPATH, "//android.widget.RelativeLayout["
                                                        "@content-desc='搜索栏']/android.widget.ImageView[1]")
        # 搜索页面的搜索栏
        self.search_bar = (AppiumBy.ID, "com.jd.lib.search.feature:id/aaf")
        # 搜索按钮
        self.search_button = (AppiumBy.ID, "com.jd.lib.search.feature:id/a_e")

    def enter_mine_page(self):
        """
        进入“我的”页面
        :return: None
        """
        self.click_el(self.mine_button)

    def search_product(self, product_name: str):
        """
        搜索商品名称:
        1.点击主页的搜索按钮
        2.在搜索页面输入商品名称
        3.点击搜索按钮
        :param product_name: 商品名称
        :return: None
        """
        self.click_el(self.home_page_search_button)
        self.input(self.search_bar, product_name)
        self.click_el(self.search_button)


if __name__ == '__main__':
    home_page = HomePage()
    # home_page.enter_mine_page()
    home_page.search_product("李宁闪击9td")
    time.sleep(5)
    DriverTools.quit_driver()
