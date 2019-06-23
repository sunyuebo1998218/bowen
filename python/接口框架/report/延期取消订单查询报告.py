from HTMLTestReportCN import HTMLTestRunner
import unittest
from 接口框架.test.延期取消订单查询_test import yanqi
def baogao(*x):
    suit=unittest.TestSuite()
    for i in x:
        suit.addTest(yanqi(i))
    f=open('c.html','wb')
    runner=HTMLTestRunner(stream=f,tester='sunyuebo',description='结果如下',title='延期取消订单报告',verbosity=2)
    runner.run(suit)
# baogao('test_1','test_2')

