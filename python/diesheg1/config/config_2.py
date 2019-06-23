from HTMLTestReportCN import HTMLTestRunner
import unittest
def report(test,report_path):
    su=unittest.TestSuite()
    su.addTest(test)
    with open(report_path,'wb')as fb:
        x=HTMLTestRunner(
            stream=fb,
            title='报告名称',
            description='报告描述',
            verbosity=2,
        )
        x.run(su)