from time import sleep

from appium import webdriver

from config import cap
from tool.get_log import GetLogger

log = GetLogger.get_log()


class GetDriver:
    __driver1 = None
    __driver2 = None
    __driver3 = None

    @classmethod
    def get_app_driver(cls):
        log.info(f"正在获取app驱动对象，启动参数是{cap}")
        if cls.__driver1 is None:
            cls.__driver1 = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)
            return cls.__driver1
        else:
            return cls.__driver1

    @classmethod
    def quit_app_driver(cls):
        log.info('关闭驱动对象，并置空')
        cls.__driver1.terminate_app('com.izaodao.french')
        cls.__driver1.quit()
        cls.__driver1 = None

