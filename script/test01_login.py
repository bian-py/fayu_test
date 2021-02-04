import allure
import page
from page.page_login import PageLogin
from tool.get_driver import GetDriver
from tool.get_log import GetLogger

log = GetLogger.get_log()


@allure.feature("我的页面业务功能测试")
class TestLogin():

    @classmethod
    def setup_class(cls):
        cls.driver = GetDriver.get_app_driver()
        cls.login = PageLogin(cls.driver)
        cls.login.base_click_element(page.approve)

    @classmethod
    def teardown_class(cls):
        GetDriver.quit_app_driver()

    @allure.story("测试登录业务功能")
    def test01_login(self):
        log.info("调用登录业务组合方法")
        self.login.pagelogin()
        try:
            log.info("正在进行断言，判断是否登录成功")
            assert self.login.base_find_element(page.login_username)
            log.info("断言成功")
        except Exception:
            log.info("断言失败")
            raise
