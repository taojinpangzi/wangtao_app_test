import time
from appium import webdriver


desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '13'
desired_caps['deviceName'] = 'realme'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
desired_caps['noReset'] = True
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element(value="com.android.settings:id/animated_hint").click()
driver.find_element(value="com.android.settings:id/search_src_text").send_keys("你好")
print(driver.find_element(value="com.android.settings:id/search_src_text").get_attribute("enabled"))
print(driver.find_element(value="com.android.settings:id/search_src_text").get_attribute("name"))
time.sleep(10)
driver.quit()
