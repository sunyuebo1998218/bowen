from HTMLTestReportCN import HTMLTestRunner
import unittest
from 接口框架.test.dingdan_test import d_dan
def baogao():
    suit=unittest.TestSuite()
    # # for i in name:
    # #第一个参数存放脚本路径，第二参数匹配测试文件的通配符
    # #函数的意思是可以自动去发现写的通配符语句中符合通配符的文件中以.test开头的函数，提取出来放在discover中
    # discover=unittest.defaultTestLoader.discover(r'E:\python\接口框架\test',pattern='.py')
    # print(discover)
    # for i in discover:
    suit.addTest(d_dan('test_1'))
    f=open('abc.html','wb')
    runner=HTMLTestRunner(stream=f,tester='sunyuebo',description='结果如下',title='别克测试报告')
    runner.run(suit)
baogao()
