import page
from base.base import Base
from tool.get_log import GetLogger

log = GetLogger.get_log()

class PageGlsx(Base):

    # �������ʦѧtab
    def pageglsx_click_menu(self):
        self.base_click_element(page.glsx_menu)
