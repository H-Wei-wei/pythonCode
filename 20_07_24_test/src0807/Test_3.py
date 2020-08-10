
# 数据驱动

# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time
import sys, csv
from ddt import ddt, data, unpack, file_data


def getCsv(file_name):
    rows = []
    path = sys.path[0]
    with open(path + '/data/' + file_name, 'rt') as f:
        readers = csv.reader(f, delimiter=',', quotechar='|')
        next(readers, None)
        for row in readers:
            temprows = []
            for i in row:
                temprows.append(i)
            rows.append(temprows)
        return rows

# 引入ddt
@ddt
class Testddt(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    # test fixture，清除环境
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    # 测试用例，必须以test开头
    # 增加ddt数据
    # 单变更时不使用unpack
    @unittest.skip("skipping")
    @data('selenium', u'测试中文', '三十而已')
    def test_baidu(self, value):
        drive = self.driver
        drive.get(self.base_url)
        drive.maximize_window()
        drive.find_element_by_id("kw").clear()
        drive.find_element_by_id("kw").send_keys(value)
        drive.find_element_by_id("su").click()
        time.sleep(5)

    @unittest.skip("skipping")
    @data(["selenium", "selenium_百度搜索"], ["测试", "测试_百度搜索"])
    @unpack
    def test_baidu2(self, key, value):
        drive = self.driver
        drive.get(self.base_url)
        drive.maximize_window()
        drive.find_element_by_id("kw").clear()
        drive.find_element_by_id("kw").send_keys(key)
        drive.find_element_by_id("su").click()
        self.assertEqual(drive.title, value, msg="not equal")
        time.sleep(5)

    @file_data('test_baidu_data.json')
    # @data(*getCsv('test_baidu_data.txt')
    # (["selenium", "selenium_百度搜索"], ["测试", "测试_百度搜索"])
    # @unpack
    def test_baidu3(self, value):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(6)
        # self.assertEqual(driver.title, value, msg="搜索结果和期望不一致")
        # time.sleep(3)

if __name__ == "__main__":
    # 执行用例
    unittest.main()
