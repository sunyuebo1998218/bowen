from 接口框架.config.peijian import Ding_Dan
from 接口框架.data.dingdan_duqu import shuju
import unittest
class dingdan(unittest.TestCase):
    s=shuju()
    def test_2(self):
        c=Ding_Dan().cha_mingxi(int(self.s[0][0]))
        print(c)
        self.assertEqual(c[''],'处理成功')
if __name__ == '__main__':
    unittest.main()