from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from config import *


class Operation:
    def __init__(self):
        desired_capabilities = dict()
        desired_capabilities['platformName'] = PLATFORM_NAME
        desired_capabilities['platformVersion'] = PLATFORM_VERSION
        desired_capabilities['deviceName'] = DEVICE_NAME
        desired_capabilities['appPackage'] = APP_PACKAGE
        desired_capabilities['appActivity'] = APP_ACTIVITY
        desired_capabilities['noReset'] = NO_RESET
        self.driver = webdriver.Remote(APPIUM_SERVER_URL, desired_capabilities)

    def quit_driver(self):
        self.driver.quit()

    # 显示等待
    def explicit_wait_xpath(self, location, timeout=10) -> WebElement:
        """
        :param location: 元素定位
        :param timeout: 显示等待的超时时间
        :return: 显示等待的元素
        """
        return (WebDriverWait(self.driver, timeout, 0.1).
                until(lambda x: x.find_element(AppiumBy.XPATH, location)))

    def tap_xpath(self, location):
        TouchAction(self.driver).tap(self.driver.find_element(AppiumBy.XPATH, location)).perform()

    def tap_coordinate(self, x_coordinate, y_coordinate):
        TouchAction(self.driver).tap(x=x_coordinate, y=y_coordinate).perform()

    def click_xpath(self, location):
        self.driver.find_element(AppiumBy.XPATH, location).click()
