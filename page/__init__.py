from selenium.webdriver.common.by import By

# 授权页面
approve = By.ID, "com.izaodao.french:id/jurisdiction_cradtv6"

# 学习页面配置信息
xx_zmjj = By.XPATH, '//android.view.View[@content-desc="Aa Bb Cc Dd Ee Ff Gg"]/../../../android.widget.FrameLayout[1]//android.widget.ImageView'
xx_zmxx1 = By.XPATH, '//android.view.View[@content-desc="Aa Bb Cc Dd Ee Ff Gg"]'
xx_menu = By.XPATH, '(//android.view.View[@content-desc="学习"])'

'''
——————————————————————————————————————————————————————————————
我的页面
_____________________________________________________________
'''

# 字母讲解视频配置信息
zm_frame = By.ID, "com.izaodao.french:id/gestureMask"
#fgjgffghf
zm_shipin_back = By.ID, 'com.izaodao.french:id/ivBack'

zm_shipin_pause = By.ID, 'com.izaodao.french:id/ivPlayBtn'

# 字母学习也配置信息
zmxx_mask = By.XPATH, '//android.view.View[@content-desc="A-G"]/../../' \
                      'android.widget.FrameLayout[2]/android.widget.ImageView[3]'
zmxx_title = By.XPATH, '//android.view.View[@content-desc="A-G"]'
zmxx_C = By.XPATH, '//android.view.View[@content-desc="C"]'
zmxx_back_btn = By.XPATH, '//android.view.View[@content-desc="A-G"]/../android.widget.FrameLayout[1]'
zmxx_confirm_back = By.XPATH, '//android.view.View[@content-desc="确认退出"]'
zmxx_swipe_area = By.ID, "com.izaodao.french:id/layout_container"

# 跟老师学配置信息
glsx_menu = By.XPATH, '//android.view.View[@content-desc="跟老师学"]'
glsx_mfbm = By.XPATH, '//android.view.View[@content-desc="免费报名"]'

# 我的页面配置信息
wd_menu = By.XPATH, '//android.view.View[@content-desc="我的"]'
unlogin = By.XPATH, '//android.view.View[@content-desc="未登录"]'
login_username = By.XPATH, '//android.view.View[@content-desc="边天一"]'

# 一键登录
login_btn = By.ID, 'com.izaodao.french:id/authsdk_login_view'

# 字母表
zmb = By.XPATH, '(//android.view.View[@content-desc="字母表"])[1]'
zmb_back_btn = By.XPATH, '//android.widget.FrameLayout[@content-desc="返回"]'
