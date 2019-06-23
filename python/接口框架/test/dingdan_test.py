from 接口框架.config.diangdan import dingdan
from 接口框架.data.dingdan_duqu import shuju
import unittest
class d_dan(unittest.TestCase):
    s=shuju()
    def test_1(self):
        b=dingdan().chaming(int(self.s[0][0]))
        print(b)
        self.assertEqual(b['totalSize'],0)
if __name__ == '__main__':
    unittest.main()