import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.connectiontype import ConnectionType

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '13'
desired_caps['deviceName'] = 'realme'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
desired_caps['noReset'] = True
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.open_notifications()
time.sleep(2)
driver.press_keycode(4)
time.sleep(10)
driver.quit()

