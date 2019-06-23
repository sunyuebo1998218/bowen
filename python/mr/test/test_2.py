from appium import webdriver
from time import sleep
import unittest
from mr.config import cnnfig_2
from mr.config .config_3 import get_logger
log=get_logger(name='test')

class mr(unittest.TestCase):
    def setUp(self):
        self.des = {
            "device": "android",
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "bc0d9588",
            "appPackage": "com.mooreshare.app",
            "appActivity": ".ui.activity.splash.SplashActivity",
            "noReset": "true",
        }
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
        sleep(5)
        log.info("手机与appium服务器建立连接")
    def test(self):
        self.dr.find_element_by_id('com.mooreshare.app:id/ll_title').click()
        sleep(2)
        try:
            a=self.dr.find_element_by_class_name('android.widget.RelativeLayout').find_element_by_class_name('android.widget.TextView').text
            self.assertEqual(a, "热门视频", msg="跳转成功")
            print('热门视频跳转成功')
        except:
            b= self.dr.find_element_by_id('com.mooreshare.app:id/rl_last_news').find_elements_by_class_name('android.widget.TextView')[0].text
            self.assertEqual(b,'即 时',msg='跳转失败')
            print('跳转失败')
        self.dr.find_element_by_id('com.mooreshare.app:id/rl_back').click()
        sleep(2)
        self.dr.find_element_by_id('com.mooreshare.app:id/ll_button_navi').find_elements_by_id('com.mooreshare.app:id/vg_button_navi')[2].click()
        sleep(2)
        try:
            c=self.dr.find_element_by_id('com.mooreshare.app:id/tv_bar_title').text
            self.assertEqual(c,'会议活动',msg='跳转成功')
            print('会议活动跳转成功')
        except:
            d= self.dr.find_element_by_id('com.mooreshare.app:id/rl_last_news').find_elements_by_class_name('android.widget.TextView')[0].text
            self.assertEqual(d,'即 时',msg='跳转失败')
            print('会议活动跳转失败')
        self.dr.find_element_by_id('com.mooreshare.app:id/rl_back').click()
        sleep(2)
        self.dr.find_element_by_id('com.mooreshare.app:id/ll_button_navi').find_elements_by_id('com.mooreshare.app:id/vg_button_navi')[1].click()
        sleep(2)
        try:
            c = self.dr.find_element_by_id('com.mooreshare.app:id/tv_bar_title').text
            self.assertEqual(c, '行业日报', msg='跳转成功')
            print('行业日报跳转成功')
        except:
            d = self.dr.find_element_by_id('com.mooreshare.app:id/rl_last_news').find_elements_by_class_name(
                'android.widget.TextView')[0].text
            self.assertEqual(d, '即 时', msg='跳转失败')
            print('行业日报跳转失败')
        self.dr.find_element_by_id('com.mooreshare.app:id/rl_back').click()
        sleep(2)
        self.dr.find_element_by_id('com.mooreshare.app:id/ll_button_navi').find_elements_by_id('com.mooreshare.app:id/vg_button_navi')[3].click()
        sleep(2)
        try:
            c = self.dr.find_element_by_id('com.mooreshare.app:id/tv_bar_title').text
            self.assertEqual(c, '芯片设计', msg='跳转成功')
            print('芯片设计跳转成功')
        except:
            d = self.dr.find_element_by_id('com.mooreshare.app:id/rl_last_news').find_elements_by_class_name(
                'android.widget.TextView')[0].text
            self.assertEqual(d, '即 时', msg='跳转失败')
            print('行业日报跳转失败')
        self.dr.find_element_by_id('com.mooreshare.app:id/rl_back').click()
        sleep(2)
        self.dr.find_element_by_id('com.mooreshare.app:id/ll_button_navi').find_elements_by_id('com.mooreshare.app:id/vg_button_navi')[4].click()
        sleep(2)
        try:
            c = self.dr.find_element_by_id('com.mooreshare.app:id/tv_bar_title').text
            self.assertEqual(c, '专题报道(73)', msg='跳转成功')
            print('专题报道(73)跳转成功')
        except:
            d = self.dr.find_element_by_id('com.mooreshare.app:id/rl_last_news').find_elements_by_class_name(
                'android.widget.TextView')[0].text
            self.assertEqual(d, '即 时', msg='跳转失败')
            print('专题报道(73)跳转失败')
        self.dr.find_element_by_id('com.mooreshare.app:id/rl_back').click()
        sleep(2)

    def tearDown(self):
        self.dr.quit()
        log.info('手机与appium服务器断开连接')

if __name__ == '__main__':
    # unittest.main()
    cnnfig_2.report(test_name=mr('test'), report_path=r"E:\python\mr\report\a.html")