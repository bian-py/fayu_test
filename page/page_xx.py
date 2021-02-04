from time import sleep

from selenium.webdriver.common.by import By

import page
from base.base import Base


class PageXx(Base):

    # �����ĸ������Ƶ
    def pagexx_click_zmjj(self):
        self.base_click_element(page.xx_zmjj)

    # �����Ƶ��ͣ
    def pagexx_click_pause(self):
        while True:
            self.base_click_element(page.zm_frame)
            try:
                self.base_find_element(page.zm_shipin_pause)
                self.base_click_element(page.zm_shipin_pause)
                break
            except:
                pass

    # �����Ƶ���ذ�ť������ѧϰҳ��
    def pagexx_click_back(self):
        while True:
            self.base_click_element(page.zm_frame)
            try:
                self.base_find_element(page.zm_shipin_back)
                self.base_click_element(page.zm_shipin_back)
                break
            except:
                pass

    # �����ĸѧϰҳ��
    def pagexx_click_zmxx(self):
        sleep(3)
        self.base_click_element(page.xx_zmxx1)

    # �����ĸѧϰ�ɲ�
    def pagexx_zmxx_click_mask(self):
        self.base_click_element(page.zmxx_mask)
        # try:
        #     self.base_click_element(page.zmxx_mask)
        # except:
        #     pass

    # ������ĸC
    def pagexx_find_C(self):
        return self.base_left_to_right_find_element(page.zmxx_swipe_area,page.zmxx_C)

    # ������ĸ%%%��demoʧ���������ݣ�
    def pagexx_find_demo(self):
        return self.base_left_to_right_find_element(page.zmxx_swipe_area,(By.XPATH, '//android.view.View[@content-desc="%%%%"]'))

    # �����ĸѧϰ���ذ�ť
    def pagexx_zmxx_click_back(self):
        self.base_click_element(page.zmxx_back_btn)
        self.base_click_element(page.zmxx_confirm_back)

    # �����ĸ��ť
    def pagexx_click_zmb(self):
        sleep(2)
        self.base_click_element(page.zmb)

    # �����ĸ���ذ�ť
    def pagexx_click_zmb_back(self):
        self.base_click_element(page.zmb_back_btn)