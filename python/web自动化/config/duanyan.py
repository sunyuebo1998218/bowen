import unittest
from web自动化.test.mr_test import mr
from web自动化.data.导入数据 import shuju
s=shuju()
class duanyan(unittest.TestCase):

    def test_1(self):
        for i in s:
            b=mr(i)
            self.assertNotEqual(b,'抱歉，没有查到任何结果')
    # def test_2(self):
    #     for i in s:
    #         c=mr(i)
    #         self.assertEqual([c],i)


if __name__ == '__main__':
    unittest.main()





