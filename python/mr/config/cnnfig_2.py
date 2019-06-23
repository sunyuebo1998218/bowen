from HTMLTestReportCN import HTMLTestRunner
import unittest


def report(test_name, report_path):
    """盘，
    :param test_name: 测试用例的名字
    :param report_path: 测试报告html的路径+名字
    :return:
    """
    # 第一步：创一个测试套件，理解成玩具枪的弹夹
    suite = unittest.TestSuite()
    # 第二步：向测试套件里面添加测试用例，理解成玩具枪弹夹添加bb弹【子弹】
    suite.addTest(test_name)
    # for i in test_name[0]:
    #     suite.addTest(i)

    # 第三步：将生成的测试结果写入html文件里，理解成玩具枪上档

    with open(report_path, 'wb') as fb:
        runner = HTMLTestRunner(
            stream=fb,
            title="报告名称",
            description="报告的描述",
            verbosity=2,
            # 输出内容的详细等级，默认是0，2代表最详细
        )
        # 执行测试用例，并声称Html测试报告， 理解成玩具枪发射子弹
        runner.run(suite)