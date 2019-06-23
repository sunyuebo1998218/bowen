# 将day1文件中的代码导入到day2中
# import day1
# day1.a()
# python中类似于day1这样的文件被称作模块
# 模块分类：
# 1.python自带的模块
# 2.需要下载的模块（第三方模块）
#
# from day1 import a,b #将 day1文件中的 a函数导入过来
# import random
# import copy
# a()
# b()
#
# #客户端
# import  socket
# #创建套接字
# while True:
#     sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #连接服务器
#
#     sock.connect(("192.168.0.88",3000))
# #将qq当做请求发送给服务器
#
#     qq =input(">>")
#     # if qq==exit:
#     #     break
#     sock.send(qq.encode("utf-8"))
# #接收响应
#     ww = sock .recv(1024)
#     print(ww.decode("utf-8"))
#
#
#
#
# udp 的客户端
# import  socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# while True:
#     host=("192.168.0.88",3000)
#     msg=input(">>>")
#     s.sendto(msg.encode("utf-8"),host)
#     reg=s.recv(1024)
#     print(reg.decode("utf-8"))
#
#
# import smtplib
# import email.mime.multipart as mul
# import email.mime.text as text
# ww=["1004745584@qq.com","17630171326@163.com"]
# message=mul.MIMEMultipart()
# message["subject"]="python_test"
# message["From"]="17629712980@163.com"
# message["To"]=".".join(ww)
#
# txt="""
#     河南你好
#     中国你好
# """
# tet=text.MIMEText(txt)
# message.attach(tet)
# smtp123=smtplib.SMTP_SSL("smtp.163.com",465)
# smtp123.login("17629712980@163.com","A1998218")
# smtp123.sendmail("17629712980@163.com",ww,message.as_string())
# smtp123.close()

# unittest 单元测试模块
# 导入函数
# 生成html测试报告
# import HTMLTestReportCN
#用于单元测试，验证预期结果与实际结果是否一致，一致代表通过，不一致代表失败
# import unittest
# class T(unittest.TestCase):
#     #必须以test开头
#     def test_1(self):
#         #预期结果
#         x='劳斯莱斯'
#         #实际结果
#         y='劳斯莱斯'
#         #第一个断言方法，判断预期结果与实际结果是否相等
#         self.assertEqual(x,y,msg='msg的作用就是填写备注信息')
#
# if __name__ == '__main__':
# #使用unittest类的main方法，自动加载当前脚本中的类，并自动运行测试用例
#     # unittest.main()
#     #生成测试报告
#     #第一步：创建一个测试套件，理解成玩具枪的弹夹
#     su=unittest.TestSuite()
#     #想测试套件添加测试用例，理解像弹夹里添加子弹
#     su.addTest(T('test_1'))
#     #第三步将生成测试结果写入html文件里
#     with open('a.html','wb')as fb:
#         x=HTMLTestReportCN.HTMLTestRunner(
#             stream=fb,
#             title='报告名称',
#             description='报告描述',
#             verbosity=2,#输出内容详细等级，默认是0,2代表详细
#         )
# #执行测试用例，并生成html测试报告
#         x.run(su)

from HTMLTestReportCN import HTMLTestRunner
from appium import webdriver
from time import sleep
import unittest
from diesheg.config import config_1
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
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('17629712980')
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('a1998218')
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
        sleep(5)
        a = self.dr.find_element_by_id('android:id/tabs').find_elements_by_id('com.qk.butterfly:id/tv_tab')[0].text
        print(a)
        self.assertEqual(a,'首页',msg='断言已经登陆成功')
if __name__ == '__main__':
    unittest.main()
    tc=DS()
    tc.setUp()
    tc.test()
