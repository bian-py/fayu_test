from time import sleep

from selenium.webdriver.common.by import By

import page
from base.base import Base


class PageXx(Base):

    # 点击字母讲解视频
    def pagexx_click_zmjj(self):
        self.base_click_element(page.xx_zmjj)

    # 点击视频暂停
    def pagexx_click_pause(self):
        while True:
            self.base_click_element(page.zm_frame)
            try:
                self.base_find_element(page.zm_shipin_pause)
                self.base_click_element(page.zm_shipin_pause)
                break
            except:
                pass

    # 点击视频返回按钮，返回学习页面
    def pagexx_click_back(self):
        while True:
            self.base_click_element(page.zm_frame)
            try:
                self.base_find_element(page.zm_shipin_back)
                self.base_click_element(page.zm_shipin_back)
                break
            except:
                pass

    # 点击字母学习页面
    def pagexx_click_zmxx(self):
        sleep(3)
        self.base_click_element(page.xx_zmxx1)

    # 点击字母学习蒙层
    def pagexx_zmxx_click_mask(self):
        self.base_click_element(page.zmxx_mask)
        # try:
        #     self.base_click_element(page.zmxx_mask)
        # except:
        #     pass

    # 查找字母C
    def pagexx_find_C(self):
        return self.base_left_to_right_find_element(page.zmxx_swipe_area,page.zmxx_C)

    # 查找字母%%%（demo失败用例数据）
    def pagexx_find_demo(self):
        return self.base_left_to_right_find_element(page.zmxx_swipe_area,(By.XPATH, '//android.view.View[@content-desc="%%%%"]'))

    # 点击字母学习返回按钮
    def pagexx_zmxx_click_back(self):
        self.base_click_element(page.zmxx_back_btn)
        self.base_click_element(page.zmxx_confirm_back)

    # 点击字母表按钮
    def pagexx_click_zmb(self):
        sleep(2)
        self.base_click_element(page.zmb)

    # 点击字母表返回按钮
    def pagexx_click_zmb_back(self):
        self.base_click_element(page.zmb_back_btn)