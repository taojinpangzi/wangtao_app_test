from appium.webdriver import WebElement
from appium.webdriver.common.touch_action import TouchAction
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

    def tap_el(self, el: WebElement):
        """
        轻敲元素
        :param el: 元素
        :return: None
        """
        TouchAction(self.driver).tap(el).perform()

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
        :return:
        """
        self.find_el(location, timeout=timeout_click).click()
