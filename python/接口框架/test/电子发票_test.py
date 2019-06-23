from 接口框架.config.电子发票明细 import dzfp
import unittest
class duanyan(unittest.TestCase):
    def test_1(self):
        b=dzfp().mx()
        self.assertEqual(b['totalSize'],0)
    def test_2(self):
        c=dzfp().mx()
        self.assertEqual(c['status'],1)

if __name__ == '__main__':
    unittest.main()