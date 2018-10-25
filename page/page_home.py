# -*- coding=utf-8 -*-
import time

from selenium.webdriver.common.by import By

from base.baseaction import Baseaction


class HomePageAction(Baseaction):
    into_btn_feature = By.ID,"com.tpshop.malls:id/start_Button"
    home_btn_faeture = By.XPATH,("text,首页,1","resource-id,com.tpshop.malls:id/tab_txtv,1")

    # 给 home 模型定义了一个动作，可以实现自动进入首页的操作
    def auto_enter_home(self):

        # 通过强制等待让加载界面消失
        time.sleep( 3 )
        try:
            self.find_element(self.home_btn_faeture)
            print("欢迎进入TPshop商城")
        except Exception:
            for i in range(3):
                self.swipe_left()
                time.sleep(0.7)
            self.click(self.into_btn_feature)

        # 执行三次滑屏操作 【因此这个操作具有通用性，所以我们选择将它放置于Base当中】
