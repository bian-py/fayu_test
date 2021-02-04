import page
from base.base import Base


class PageLogin(Base):

    # ����ҵ�tab
    def pagelogin_click_mine(self):
        self.base_click_element(page.wd_menu)

    # ����һ����¼��ť
    def pagelogin_call_login(self):
        self.base_click_element(page.unlogin)

    # �����¼��ť
    def pagelogin_click_login(self):
        self.base_click_element(page.login_btn)

    # ��¼ҵ����Ϸ���
    def pagelogin(self):
        self.pagelogin_click_mine()
        self.pagelogin_call_login()
        self.pagelogin_click_login()