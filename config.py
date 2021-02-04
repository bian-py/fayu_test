import os

# 文件路径配置信息
BASE_PATH = os.path.dirname(__file__)

cap = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "HJS0218B27006432",
    "appPackage": "com.izaodao.french",
    # "appActivity": ".activity.SplashActivity",
    # "appWaitActivity":".activity.JurisdictionActivity",
    "appActivity": ".activity.SplashActivity",
    # "newCommandTimeout": 600,
    "recreateChromeDriverSessions": True,
    # "autoGrantPermissions": True
}

