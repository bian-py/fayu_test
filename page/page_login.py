import page
from base.base import Base


class PageLogin(Base):

    # 点击我的tab
    def pagelogin_click_mine(self):
        self.base_click_element(page.wd_menu)

    # 调出一键登录按钮
    def pagelogin_call_login(self):
        self.base_click_element(page.unlogin)

    # 点击登录按钮
    def pagelogin_click_login(self):
        self.base_click_element(page.login_btn)

    # 登录业务组合方法
    def pagelogin(self):
        self.pagelogin_click_mine()
        self.pagelogin_call_login()
        self.pagelogin_click_login()