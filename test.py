import time
from appium import webdriver


desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '13'
desired_caps['deviceName'] = 'realme'
# desired_caps['appPackage'] = 'com.android.settings'
# desired_caps['appActivity'] = '.Settings'
# desired_caps['appPackage'] = 'tv.danmaku.bili'
# desired_caps['appActivity'] = '.MainActivityV2'
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = '.ui.LauncherUI'
desired_caps['noReset'] = True
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(10)
# driver.start_activity("com.amaze.filemanager", ".activities.MainActivity")

print(driver.current_package)
print(driver.current_activity)
driver.quit()
