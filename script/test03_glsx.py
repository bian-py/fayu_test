import allure
import pytest
import page
from page.page_glsx import PageGlsx
from tool.get_driver import GetDriver
from tool.get_log import GetLogger

log = GetLogger.get_log()


@allure.feature("跟老师学页面业务功能测试")
class TestGlsx():

    @classmethod
    def setup_class(cls):
        cls.driver = GetDriver.get_app_driver()
        cls.glsx = PageGlsx(cls.driver)
        cls.glsx.base_click_element(page.approve)

    @classmethod
    def teardown_class(cls):
        GetDriver.quit_app_driver()

    @allure.story("测试跟老师学页面显示")
    def test01_glsh(self):
        log.info("点击跟老师学页面")
        self.glsx.pageglsx_click_menu()
        log.info("正在进行断言，判断是否成功跳转")
        assert self.glsx.base_find_element(page.glsx_mfbm)

    @allure.story("测试跟老师学页面显示——故障情况")
    def test02_glsh(self):
        log.info("点击跟老师学页面——定位元素故障")
        self.glsx.base_find_element(page.approve)

    @pytest.mark.skip(reason="demo设置跳过")
    @allure.story("测试跟老师学页面显示")
    def test03_glsh(self):
        log.info("点击跟老师学页面")
        self.glsx.pageglsx_click_menu()
        log.info("正在进行断言，判断是否成功跳转")
        assert self.glsx.base_find_element(page.glsx_mfbm)
