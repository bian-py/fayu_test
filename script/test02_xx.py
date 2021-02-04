import os
from time import sleep
import allure
import page
from page.page_login import PageLogin
from page.page_xx import PageXx
from tool.get_driver import GetDriver
from tool.get_log import GetLogger

log = GetLogger.get_log()
module_name = str(os.path.basename(__file__)).split('.')[0]


@allure.feature("学习页面业务功能测试")
class TestXx():
    @classmethod
    def setup_class(cls):
        cls.driver = GetDriver.get_app_driver()
        cls.xx = PageXx(cls.driver)
        cls.xx.base_click_element(page.approve)
        PageLogin(cls.driver).pagelogin()
        cls.xx.base_click_element(page.xx_menu)

    @classmethod
    def teardown_class(cls):
        GetDriver.quit_app_driver()

    @allure.story("测试字母表显示功能")
    def test01_zimubiao(self):
        log.info("进入字母表页")
        self.xx.pagexx_click_zmb()
        log.info("正在进行断言（简化处理，demo这里写死）")
        assert True
        log.info("返回学习主页面")
        self.xx.pagexx_click_zmb_back()

    @allure.story("测试视频播放/暂停功能")
    def test02_shipin(self):
        log.info("进入字母讲解视频，查看视频播放情况")
        sleep(2)
        self.xx.pagexx_click_zmjj()
        log.info("正在进行断言（简化处理，demo这里写死）")
        assert True
        sleep(2)
        log.info("正在调出视频控制菜单，点击暂停按钮")
        log.info("进入字母讲解视频")
        self.xx.pagexx_click_pause()
        log.info("正在进行断言（简化处理，demo这里写死）")
        assert True
        log.info("返回学习主页面")
        self.xx.pagexx_click_back()
        sleep(2)

    @allure.story("测试字母学习功能是否完整")
    def test03_zmxx(self):
        log.info("点击进入字母学习页面")
        with allure.step("点击进入学习页面"):
            pass
        self.xx.pagexx_click_zmxx()
        log.info("点击蒙屏菜单按钮")
        with allure.step("点击蒙屏菜单按钮"):
            pass
        self.xx.pagexx_zmxx_click_mask()
        with allure.step("开始进行查找操作"):
            allure.attach("找到字母C", "结果返回TRUE,断言成功")
            allure.attach("未找到字母C", "滑动继续寻找，未找到返回FALSE")
        with allure.step("开始进行断言"):
            allure.attach("判断返回值为TRUE", "断言成功")
            allure.attach("判断返回值为FALSE", "断言失败")
            try:
                log.info("正在进行断言，判断字母学习中是否存在字符C")
                assert self.xx.pagexx_find_C()
                log.info("断言成功，找到字母")
            except:
                log.error("断言失败")
                raise
            finally:
                log.info("返回学习主页面")
                self.xx.pagexx_zmxx_click_back()

    @allure.story("测试字母学习功能是否完整——错误情况")
    def test04_zmxx_error_demo(self):
        log.info("点击进入字母学习页面")
        with allure.step("点击进入学习页面"):
            pass
        self.xx.pagexx_click_zmxx()
        with allure.step("开始进行查找操作"):
            allure.attach("找到字母%%%", "结果返回TRUE,断言成功")
            allure.attach("未找到字母%%%", "滑动继续寻找，未找到返回FALSE")
        with allure.step("开始进行断言"):
            allure.attach("判断返回值为TRUE", "断言成功")
            allure.attach("判断返回值为FALSE", "断言失败")
            try:
                log.info("正在进行断言，判断字母学习中是否存在字符%%%%")
                assert self.xx.pagexx_find_demo()
                log.info("断言成功，找到字母")
            except Exception:
                log.error("断言失败")
                self.xx.base_get_screenshot_as_file(module_name)
                raise
            finally:
                log.info("返回学习主页面")
                self.xx.pagexx_zmxx_click_back()
