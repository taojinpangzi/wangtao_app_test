from appium import webdriver
from config import *


class DriverTools:
    __driver = None

    @classmethod
    def get_driver(cls):
        """
        初始化driver，这里是同一个driver对象可以在两个页面类中可以保持的关键：
        举例：第一个页面类时，初始化driver，第一个页面类完成后，进入第二个页面类，此时
        cls.__driver is not None，进入else判断，使用前面的driver，而不用初始化
        :return:
        """
        if cls.__driver is None:
            __desired_capabilities = dict()
            __desired_capabilities['platformName'] = PLATFORM_NAME
            __desired_capabilities['platformVersion'] = PLATFORM_VERSION
            __desired_capabilities['deviceName'] = DEVICE_NAME
            __desired_capabilities['appPackage'] = APP_PACKAGE
            __desired_capabilities['appActivity'] = APP_ACTIVITY
            __desired_capabilities['noReset'] = NO_RESET
            cls.__driver = webdriver.Remote(APPIUM_SERVER_URL, __desired_capabilities)
            return cls.__driver
        else:
            return cls.__driver

    @classmethod
    def quit_driver(cls):
        if cls.__driver:
            cls.__driver.quit()
            cls.__driver = None


if __name__ == '__main__':
    driver = DriverTools.get_driver()
    DriverTools.quit_driver()
