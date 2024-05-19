import os

# 连接真机/模拟器的desired_capabilities字典信息
PLATFORM_NAME = "Android"
PLATFORM_VERSION = "13"
DEVICE_NAME = "192.168.31.111:5555"
APP_PACKAGE = "com.jingdong.app.mall"
APP_ACTIVITY = ".main.MainActivity"
NO_RESET = True
APPIUM_SERVER_URL = "http://localhost:4723/wd/hub"

# 项目根目录路径
BASE_PATH = os.path.dirname(__file__)

# 测试数据路径
DATA_PATH = BASE_PATH + "/data/"

# 项目mysql连接信息
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PASSWORD = "123456"

# APP登陆账号/密码/验证码
USERNAME = "admin"
PASSWORD = "HM_2023_test"
