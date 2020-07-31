
# coding = utf-8
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
# 最大化窗口
browser.maximize_window()

browser.find_element_by_id("kw").send_keys("刘些宁")
browser.find_element_by_id("su").click()

# 固定等待
# time.sleep(10)

# 智能等待
browser.implicitly_wait(10)

browser.find_element_by_link_text("刘些宁_百度百科").click()

time.sleep(6)
browser.quit()