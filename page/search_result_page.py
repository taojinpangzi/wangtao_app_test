import time
from appium.webdriver.common.appiumby import AppiumBy
from common.base import Base
from common.driver_tools import DriverTools
from page.home_page import HomePage


class SearchResultPage(Base):
    def __init__(self):
        super().__init__()
        # 搜索结果页面的第一个商品图片
        self.goods_img = (AppiumBy.XPATH, "//android.widget.RelativeLayout["
                                          "1]/android.widget.RelativeLayout/android.widget.RelativeLayout["
                                          "1]/android.widget.ImageView")

    def enter_goods_detail_page(self):
        self.click_el(self.goods_img)


if __name__ == '__main__':
    home_page = HomePage()
    home_page.search_product("李宁闪击9td")
    SearchResultPage().enter_goods_detail_page()
    time.sleep(5)
    DriverTools.quit_driver()
