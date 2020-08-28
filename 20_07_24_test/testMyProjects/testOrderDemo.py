
from selenium import webdriver
import time
import unittest

class TestOrderDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(6)
        self.driver.quit()

    def login(self):
        self.driver.find_element_by_id()


    def register(self):
        self.driver.get("http://39.106.225.108:8080/java_order_system/index.html")
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/nav/div[1]/div[1]/div[1]/div[2]/div").click()
        time.sleep(6)
        div = self.driver.find_element_by_xpath("//*[@id=\"app\"]/div[3]")
        div.find_element_by_xpath("//*[@id=\"input-53\"]").send_keys(U"二十")
        div.find_element_by_xpath("//*[@id=\"input-56\"]").send_keys("1212")
        time.sleep(3)
        div.find_element_by_xpath("//*[@id=\"app\"]/div[3]/div/div/div[2]/div/div[3]/div[1]/button/span").click()

if __name__=="__main__":
    unittest.main()
