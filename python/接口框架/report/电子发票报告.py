from HTMLTestReportCN import HTMLTestRunner
import unittest
from 接口框架.test.电子发票_test import duanyan
def baogao(*x):
    suit=unittest.TestSuite()
    for i in x:
        suit.addTest(duanyan(i))
    f=open('c.html','wb')
    runner=HTMLTestRunner(stream=f,tester='sunyuebo',description='结果如下',title='电子发票报告',verbosity=2)
    runner.run(suit)
# baogao('test_1','test_2')