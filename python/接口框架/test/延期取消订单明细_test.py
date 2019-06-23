from 接口框架.config.延期取消订单明细 import dingdan
import unittest
class duanyan(unittest.TestCase):
    def test_1(self):
        b=dingdan().mx()
        self.assertEqual(b['totalSize'],0)
    def test_2(self):
        c=dingdan().mx()
        self.assertEqual(c['status'],1)

if __name__ == '__main__':
    unittest.main()