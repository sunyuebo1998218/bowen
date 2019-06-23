from HTMLTestReportCN import HTMLTestRunner
# from appium import webdriver
# from time import sleep
# import unittest
#  from diesheg.config import config_1
# class DS(unittest.TestCase):
#     #每个用列执行之前运行一次，作用：用于清理测试环境残留数据，初始化测试环境
#     def setUp(self):
#         self.des = {
#             "device": "android",
#             "platformName": "Android",
#             "platformVersion": "9",
#             "deviceName": "bc0d9588",
#             "appPackage": "com.qk.butterfly",
#             "appActivity": ".main.LauncherActivity",
#             "noReset": "true",
#         }
#         self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
#         sleep(5)
# # 写测试用力部分
#     def test_1(self):
#         self.dr.find_element_by_id('com.qk.butterfly:id_login_pwd').click()
#         sleep(2)
#         # 使用测试脚本与测试数据相结合
#         for i in config_1.read_data():
# #试用账号密码登录
#             self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('i[0]')
#             sleep(2)
#             self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('i[1]')
#             sleep(2)
#             self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
#
#         #断言
#         sleep(5)
#         #进入登录之后的页面
#         a=self.dr.find_elements_by_id('android:id/tabs')[0].text
#         self.assertEqual(a,'首页',msg='断言已经登陆成功')
#
#
# #每个测试用例执行完毕之后，运行teardown一次，作用：测试用例运行完，清理测试环境
#     def tearDown(self):
#         self.dr.quit()
# if __name__ == '__main__':
#     unittest.main()
#     tc=DS()
#     tc.setUp()
#     sleep(5)
#     tc.test_1()


from HTMLTestReportCN import HTMLTestRunner
from appium import webdriver
from time import sleep
import unittest
from diesheg1.config import config_1
from diesheg1.config import config_2
class DS(unittest.TestCase):
    #每个用列执行之前运行一次，作用：用于清理测试环境残留数据，初始化测试环境
    def setUp(self):
        self.des = {
            "device": "android",
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "bc0d9588",
            "appPackage": "com.qk.butterfly",
            "appActivity": ".main.LauncherActivity",
            "noReset": "true",
        }
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
        sleep(3)
    def test(self):
        self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
        sleep(3)
        # for i in config_1.read_data():
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('17629712980')
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('a1998218')
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
        sleep(5)
        try:
           if'登录'==self.dr.find_elements_by_id('com.qk.butterfly:id/tv_to_login').text:
               print('登录失败')
        except:
            a = self.dr.find_element_by_id('android:id/tabs').find_elements_by_id('com.qk.butterfly:id/tv_tab')[0].text
            print(a)
            self.assertEqual(a,'首页',msg='断言已经登陆成功')
            print('登陆成功')
    # def tearDown(self):
    #     self.dr.quit()
if __name__ == '__main__':
    # unittest.main()
    config_2.report(test=DS('test'),report_path='E:\\python\\diesheg1\\report\\a.html')
    # tc=DS()
    # tc.setUp()
    # tc.test()