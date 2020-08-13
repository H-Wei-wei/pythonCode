

# coding = utf-8
from selenium import webdriver
import unittest
import time

class TestBlogDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    # 注册
    def test_register(self):
        self.driver.get("http://127.0.0.1:8080/20_07_14_blogdemo/register.html")
        inputs = self.driver.find_elements_by_tag_name("input")
        inputs[0].send_keys("weiwei")
        inputs[1].send_keys("weiwei")
        inputs[2].click()
        self.driver.find_element_by_link_text("点击这里进行跳转").click()
        time.sleep(3)

    # 登录
    def test_login(self):
        self.driver.get("http://127.0.0.1:8080/20_07_14_blogdemo/login.html")
        inputs = self.driver.find_elements_by_tag_name("input")
        inputs[0].send_keys("123")
        inputs[1].send_keys("123")
        time.sleep(3)
        inputs[2].click()
        time.sleep(5)
        self.driver.find_element_by_link_text("点击这里进行跳转").click()
        time.sleep(3)

    def test_addArticle(self):
        # 先登录
        self.driver.get("http://127.0.0.1:8080/20_07_14_blogdemo/login.html")
        self.driver.implicitly_wait(3)
        inputs = self.driver.find_elements_by_tag_name("input")
        inputs[0].send_keys("123")
        inputs[1].send_keys("123")
        inputs[2].click()
        self.driver.find_element_by_link_text("点击这里进行跳转").click()
        # 增加文章
        index = self.driver.find_element_by_tag_name("form")
        index.find_element_by_name("title").send_keys("title6")
        index.find_element_by_name("content").send_keys("6666666666")
        index.find_element_by_xpath("/html/body/form/input[2]").click()
        time.sleep(4)
        self.driver.find_element_by_link_text("点击这里进行跳转").click()
        time.sleep(3)

    def test_deleteArticle(self):
        # 先登录
        self.driver.get("http://127.0.0.1:8080/20_07_14_blogdemo/login.html")
        self.driver.implicitly_wait(3)
        inputs = self.driver.find_elements_by_tag_name("input")
        inputs[0].send_keys("123")
        inputs[1].send_keys("123")
        inputs[2].click()
        self.driver.find_element_by_link_text("点击这里进行跳转").click()
        # 删除
        # self.driver.find_element_by_xpath("/html/body/div[1]/a[2]").click()
        divs = self.driver.find_element_by_tag_name("body").find_elements_by_tag_name("div")
        divs[6].find_element_by_link_text("删除").click()
        time.sleep(4)
        self.driver.find_element_by_link_text("点击这里进行跳转").click()
        time.sleep(3)

if __name__=="__main__":
    unittest.main()
