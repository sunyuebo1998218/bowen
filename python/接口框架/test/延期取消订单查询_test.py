from 接口框架.config.延期取消订单查询 import yqcx
import unittest
class yanqi(unittest.TestCase):
    def test_1(self):
        b=yqcx().cx()
        self.assertEqual(b['totalSize'],0)
    def test_2(self):
        c=yqcx().cx()
        self.assertEqual(c['status'],1)

if __name__ == '__main__':
    unittest.main()
