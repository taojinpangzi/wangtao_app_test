import time
from appium.webdriver.common.appiumby import AppiumBy
from common.base import Base
from common.driver_tools import DriverTools
from page.home_page import HomePage
from page.search_result_page import SearchResultPage


class GoodsDetailPage(Base):
    def __init__(self):
        super().__init__()
        # “添加购物车”按钮
        self.add_shopping_cart_button = (AppiumBy.ID, "com.jd.lib.productdetail.feature:id/b5u")

        # “立即购买”按钮
        self.buy_button = (AppiumBy.ID, "com.jd.lib.productdetail.feature:id/e")

        # “立即购买”的确定按钮
        self.buy_confirm_button = (AppiumBy.ID, "com.jd.lib.settlement.feature:id/uy")

    def buy_goods(self):
        self.click_el(self.buy_button)
        self.click_el(self.buy_confirm_button)


if __name__ == '__main__':
    home_page = HomePage()
    search_result_page = SearchResultPage()
    goods_detail_page = GoodsDetailPage()

    home_page.search_product("李宁闪击9td")
    search_result_page.enter_goods_detail_page()
    goods_detail_page.buy_goods()
    time.sleep(5)
    DriverTools.quit_driver()
