from page.goods_detail_page import *
from page.search_result_page import *


class TestEnterPaymentPage:
    def setup_class(self):
        self.driver = DriverTools.get_driver()
        self.home_page = HomePage()
        self.search_result_page = SearchResultPage()
        self.goods_detail_page = GoodsDetailPage()
        self.base = Base()

    @staticmethod
    def teardown_class():
        time.sleep(5)
        DriverTools.quit_driver()

    def test_enter_payment_success(self):
        self.home_page.search_product("李宁闪击9td")
        self.search_result_page.enter_goods_detail_page()
        self.goods_detail_page.buy_goods()
        assert self.base.find_el((AppiumBy.ID, "com.jingdong.app.mall:id/c8r")).text == "确认付款"




