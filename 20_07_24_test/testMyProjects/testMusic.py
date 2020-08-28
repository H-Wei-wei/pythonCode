
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
        # self.deleteMusic()
        # time.sleep(6)
        # self.addMusicToLove()
        # time.sleep(6)
        # self.loveMusic()
        # time.sleep(6)
        # self.removeLove()
        # time.sleep(6)
        # self.returnOne()
        # self.selIfMusic()
        self.deleteSelMusic()

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

    def addMusic(self):
        self.driver.find_element_by_link_text(U"添加歌曲").click()

    def addMusicToLove(self):
        self.driver.find_element_by_xpath("//*[@id=\"info\"]/tr[1]/td[4]/button[2]").click()
        time.sleep(3)
        alert = self.driver.switch_to.alert
        alert.accept()

    def loveMusic(self):
        self.driver.find_element_by_link_text(U"喜欢列表").click()

    def removeLove(self):
        self.driver.find_element_by_xpath("//*[@id=\"info\"]/tr/td[4]/button").click()
        time.sleep(3)
        alert = self.driver.switch_to.alert
        alert.accept()

    def returnOne(self):
        self.driver.find_element_by_link_text("回到首页").click()

    def selIfMusic(self):
        self.driver.find_element_by_id("exampleInputName2").send_keys("活")
        self.driver.find_element_by_id("submit1").click()
        time.sleep(3)
        self.driver.find_element_by_id("exampleInputName2").clear()
        self.driver.find_element_by_id("submit1").click()

    def deleteSelMusic(self):
        self.driver.find_element_by_id("28").click()
        self.driver.find_element_by_id("29").click()
        time.sleep(3)
        self.driver.find_element_by_link_text(U"删除选中").click()
        time.sleep(3)
        alert = self.driver.switch_to.alert
        alert.accept()

if __name__=="__main__":
    unittest.main()



