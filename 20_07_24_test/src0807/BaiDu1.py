
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os

class TestBaiDu1(unittest.TestCase):
    # test fixture，初始化环境
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        # print("------setUp--------")

    # test fixture，清除环境
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        # print("------tearDown--------")

    # 测试用例，必须以test开头
    @unittest.skip("skipping")
    def test_baiDuSearch(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(u"测试")
        driver.find_element_by_id("su").click()
        # driver.find_element_by_id("su").click()
        # print("------test_baiDuSearch--------")

    @unittest.skip("skipping")
    def test_baiDuSearch1(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(u"三十而已")
        driver.find_element_by_id("su").click()
        time.sleep(6)
        # 断言
        # assertEqual 是前两个参数是否相等，不相等就打印 msg 并报错
        # self.assertEqual("三十而已", driver.title, msg="不一样")
        self.assertNotEqual("三十而已", driver.title, msg="不一样")

    def test_hao(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("hao123").click()
        time.sleep(2)

    # 判断element是否存在，可删除
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    # 判断alert是否存在，可删除
    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    # 关闭alert，可删除
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True


if __name__ == "__main__":
    # 执行用例
    unittest.main()
