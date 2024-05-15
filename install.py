import time
from appium import webdriver


desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = 'xiaomi'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(3)
# driver.start_activity("com.amaze.filemanager", ".activities.MainActivity")
driver.install_app("D:/cuto-9dee5772-0ba1-4d3f-9b91-7ba3fd255fd9.apk")
driver.quit()
