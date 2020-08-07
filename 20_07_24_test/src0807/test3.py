
# 将某个类中的所有测试用例进行测试

import unittest

from src0807 import BaiDu1
from src0807 import BaiDu2

def createSuite():
    suite1 = unittest.TestLoader().loadTestsFromTestCase(BaiDu1.TestBaiDu1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(BaiDu2.TestBaiDu2)
    suite = unittest.TestSuite([suite1, suite2])
    return suite

if __name__=="__main__":
    suite = createSuite()
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)
