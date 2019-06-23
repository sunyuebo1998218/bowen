# -*- coding: utf-8 -*- 

# @Time : 2019/6/11 上午9:28 

# @Author : 废柴 

# @Project: douyun

# @FileName : test_1.py 

# @Software: PyCharm

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================

# 导入模块
import unittest
from appium import webdriver
from time import sleep
import warnings
from DieSheng.config import config_1
from DieSheng.config import config_2
from DieSheng.config.config_3 import get_logger#写日志
#创建变量接受日志的句柄--相当于一根笔
log=get_logger(name='test_1')

#testcase写测试用列的类，单元测试必须继承于unittest,Testcase
class DS(unittest.TestCase):

    # 每个用例执行之前运行一次，作用：用于清理测试环境残留数据，初始化测试环境
    def setUp(self):#相当于init，类被调用的时候，会自动运行
        warnings.simplefilter('ignore', ResourceWarning)#忽略相关警告
        self.des = {
            "device": "android",
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "bc0d9588",
            "appPackage": "com.qk.butterfly",
            "appActivity": ".main.LauncherActivity",
            "noReset": "true",
        }
        # http://127.0.0.1:4723/wd/hub 固定的，写死localhost==127.0.0.1
        # 测试脚本与appium服务器建立一个session连接
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
        sleep(5.0)
        log.info("手机与appium服务器建立连接")
    # 写测试用例的部分
    def test_1(self):
        # 使用账号密码登录蝶声
        # 点击密码，进入手机号、密码登录页面
        self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()

        # 使用脚本与测试数据相结合
        for i in config_1.read_data():

            # 进入账号密码登录页面之后
            self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(i[0])
            self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(i[1])
            self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
            # 断言
            sleep(5.0)
            """
            if else 处理登录成功与失败,也可以使用try except语句做断言
            """
            try:
                # 登录失败，页面还在登录页面
                b = self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').text
                # print("登录失败")
                self.assertEqual(b, "登录", msg="登录失败")
                print("登录失败")
            except:
                a = self.dr.find_element_by_id('android:id/tabs').find_elements_by_id('com.qk.butterfly:id/tv_tab')[
                    0].text
                print(a)
                self.assertEqual(a, '首页', msg='断言已经登陆成功')
                print('登陆成功')


    # 每个测试用例执行完毕之后，运行teardown一次，作用：测试用例运行完，清理测试环境
    def tearDown(self):#自动运行
        self.dr.quit()



if __name__ == '__main__':
    unittest.main()
    config_2.report(test_name=DS('test_1'), report_path=r"E:\python\DieSheng\report\a.html")
    # config_2.report(test_name=DS("test_1"), report_path=r"E:\python\DieSheng\report\a.html")











