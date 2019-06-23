from web自动化.config.duanyan import duanyan
from HTMLTestReportCN import HTMLTestRunner
import unittest
def baogao(*x):
    suit=unittest.TestSuite()
    for i in x:
        suit.addTest(duanyan(i))
    f=open(r'E:\python\web自动化\report\a.html','wb')
    runner=HTMLTestRunner(stream=f,tester='sunyuebo',description='结果如下',title='搜索跳转',verbosity=2)
    runner.run(suit)
# baogao('test_1')