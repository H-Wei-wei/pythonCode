
# 将某个类中的全部测试用例进行测试
import unittest

from src0807 import BaiDu1
from src0807 import BaiDu2

def createSuite():
    # 创建测试套件
    suite = unittest.TestSuite()
    # 将测试用例加入到测试套件中来
    suite.addTest(unittest.makeSuite(BaiDu1.TestBaiDu1))
    suite.addTest(unittest.makeSuite(BaiDu2.TestBaiDu2))
    return suite

if __name__=="__main__":
    suite = createSuite()
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)
