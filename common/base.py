from appium.webdriver import WebElement
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from common.driver_tools import DriverTools


class Base(object):
    def __init__(self):
        self.driver = DriverTools.get_driver()

    def find_el(self, location: tuple, timeout=10) -> WebElement:
        """
        根据location查找元素，如果找不到就抛异常
        :param location: 元素的定位，这里需要传一个tuple，比如(By.ID, "id")
        :param timeout: 显式等待的超时时间
        :return: 需要查找的元素
        """
        try:
            return (WebDriverWait(self.driver, timeout, 0.1).
                    until(lambda x: x.find_element(*location)))
        except Exception as e:
            print(f"未找到指定元素，原因为{e}")

    def tap_el(self, location: tuple, timeout_tap=10):
        """
        轻敲元素
        :param location: 元素的定位，这里需要传一个tuple，比如(By.ID, "id")
        :param timeout_tap: 显式等待的超时时间
        :return: None
        """
        TouchAction(self.driver).tap(self.find_el(location, timeout=timeout_tap)).perform()

    def tap_coordinate(self, x_coordinate: int, y_coordinate: int):
        """
        轻敲坐标
        :param x_coordinate: x坐标
        :param y_coordinate: y坐标
        :return: None
        """
        TouchAction(self.driver).tap(x=x_coordinate, y=y_coordinate).perform()

    def click_el(self, location: tuple, timeout_click=10):
        """
        点击元素
        :param timeout_click: 显式等待的超时时间
        :param location: 元素的定位，这里需要传一个tuple，比如(By.ID, "id")
        :return: None
        """
        self.find_el(location, timeout=timeout_click).click()

    def input(self, location: tuple, info: str, timeout_input=10):
        """
        输入
        :param location: 元素的定位，这里需要传一个tuple，比如(By.ID, "id")
        :param info: 需要输入的内容
        :param timeout_input: 显式等待的超时时间
        :return: None
        """
        self.find_el(location, timeout=timeout_input).send_keys(info)

    def select_option(self, location: tuple, index: int, timeout_select=10):
        """
        下拉框 选中选项元素
        :param location: 元素的定位，这里需要传一个tuple，比如(By.ID, "id")
        :param index: 需要选中的元素index
        :param timeout_select: 显式等待的超时时间
        :return: None
        """
        select = Select(self.find_el(location, timeout=timeout_select))
        select.select_by_index(index)

    def alert_confirm(self, accept: bool = True):
        """
        处理弹窗
        :param accept: 默认接受弹窗
        :return: None
        """
        alert = self.driver.switch_to.alert
        if accept:
            alert.accept()
        else:
            alert.dismiss()
