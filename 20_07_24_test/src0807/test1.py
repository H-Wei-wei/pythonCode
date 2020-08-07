
# testAdd 是将某些类的某个测试用例添加到测试套件中

# coding = utf-8
from selenium import webdriver
import time
import unittest

# 从文件中导入测试的类
from src0807 import BaiDu1
from src0807 import BaiDu2

def createSuite():
    # 创建测试套件
    suite = unittest.TestSuite()
    # 将测试用例加入到测试套件中
    suite.addTest(BaiDu1.TestBaiDu1("test_baiDuSearch"))
    suite.addTest(BaiDu1.TestBaiDu1("test_hao"))
    suite.addTest(BaiDu2.TestBaiDu2("test_baiDuSearch"))
    return suite

if __name__=="__main__":
    suite = createSuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

