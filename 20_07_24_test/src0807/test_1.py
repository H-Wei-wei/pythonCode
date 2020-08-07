
from selenium import webdriver
import unittest
import os, sys, time
import HTMLTestRunner

def createSuite():
    discovers = unittest.defaultTestLoader.discover("../src0807", pattern="BaiDu*.py", top_level_dir=None)
    print(discovers)
    return discovers

if __name__ == "__main__":
    # sys.path 是 python 的搜索模块的路径，返回结果是list
    curpath = sys.path[0]
    print(sys.path)
    print(sys.path[0])
    if not os.path.exists(curpath + "/resultreport"):
        os.makedirs(curpath + "/resultreport")
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(time.time())
    print(time.localtime())
    print(now)
    filename = curpath + "/resultreport/" + now + "resultreport.html"
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试报告", description="用例执行结果",
                                               verbosity=2)
        discovers = createSuite()
        runner.run(discovers)
