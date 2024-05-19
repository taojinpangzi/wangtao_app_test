import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_capabilities = dict()
desired_capabilities['platformName'] = "Android"
desired_capabilities['platformVersion'] = "13"
desired_capabilities['deviceName'] = "111"
desired_capabilities['appPackage'] = "com.android.chrome"
desired_capabilities['appActivity'] = "com.google.android.apps.chrome.Main"
desired_capabilities['noReset'] = True
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

url = driver.find_element(AppiumBy.ID, "com.android.chrome:id/url_bar")
url.click()
url.clear()
url.send_keys("https://m.baidu.com")
driver.press_keycode(66)
print(driver.contexts)

driver.switch_to.context(driver.contexts[-1])
driver.find_element(AppiumBy.XPATH, "//*[@id='index-kw']").send_keys("王韬")
driver.find_element(AppiumBy.XPATH, "//*[@id='index-bn']").click()

driver.quit()
