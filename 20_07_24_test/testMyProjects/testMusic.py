
from selenium import webdriver
import time
import unittest

class TestMusic(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def test_login(self):
        self.driver.get("http://39.106.225.108:8080/onlineMusic/login.html")
        self.driver.find_element_by_id("user").send_keys("微微")
        self.driver.find_element_by_id("password").send_keys("1212")
        time.sleep(6)
        self.driver.find_element_by_id("submit").click()
        time.sleep(6)
        self.deleteMusic()

    @unittest.skip("skipping")
    def test_register(self):
        # self.driver.get("http://39.106.225.108:8080/onlineMusic/login.html")
        # self.driver.find_element_by_link_text("注册").click()
        self.driver.get("http://39.106.225.108:8080/onlineMusic/register.html")
        self.driver.find_element_by_id("user").send_keys(U"星期一")
        self.driver.find_element_by_id("password").send_keys("1212")
        self.driver.find_element_by_xpath("//*[@id=\"age\"]").send_keys("18")
        self.driver.find_element_by_id("gender").send_keys("女")
        self.driver.find_element_by_id("email").send_keys("2195792949@qq.com")
        time.sleep(6)
        self.driver.find_element_by_id("submit").click()

    def deleteMusic(self):
        # self.driver.get("http://39.106.225.108:8080/onlineMusic/list.html")
        self.driver.find_element_by_xpath("//*[@id=\"info\"]/tr[1]/td[4]/button[1]").click()
        time.sleep(3)
        alert = self.driver.switch_to.alert
        alert.accept()


if __name__=="__main__":
    unittest.main()



