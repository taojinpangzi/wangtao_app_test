from selenium.webdriver.common.by import By
from common.base import *


class HomePage(Base):
    def __init__(self):
        super().__init__()
        # “我的”按钮
        self.mine_button = (By.XPATH, "//android.view.View[@content-desc='我的']")
        # homepage的搜索按钮
        self.home_page_search_button = (By.XPATH, "//android.widget.RelativeLayout["
                                                  "@content-desc='搜索栏']/android.widget.ImageView[1]")
        # 搜索页面的搜索栏
        self.search_bar = (By.ID, "com.jd.lib.search.feature:id/aaf")
        # 搜索按钮
        self.search_button = (By.ID, "com.jd.lib.search.feature:id/a_e")

    def enter_mine_page(self):
        """
        进入“我的”页面
        :return: None
        """
        self.click_el(self.mine_button)

    def search_product(self, product_name: str):
        """
        搜索商品名称
        :param product_name: 商品名称
        :return: None
        """
        self.click_el(self.home_page_search_button)
        self.input(self.search_bar, product_name)
        self.click_el(self.search_button)


if __name__ == '__main__':
    homepage = HomePage()
    homepage.enter_mine_page()
    # homepage.search_product("李宁闪击9td")
