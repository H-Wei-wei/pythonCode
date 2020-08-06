
# 多层框架/窗口定位

# coding = utf-8
from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
file_path = "file:///" + os.path.abspath("F:/Users/Administrator/Documents/selenium2html/frame.html")
driver.get(file_path)
driver.maximize_window()

# 从默认页面跳转到 frame1 页面
driver.switch_to.frame("f1")
# f1 页面跳转到 f2
driver.switch_to.frame("f2")

# 再根据属性定位元素
driver.find_element_by_id("kw").send_keys("刘些宁")
driver.find_element_by_id("su").click()

# driver.implicitly_wait(10)
# driver.find_element_by_link_text("刘些宁_百度百科").click()

time.sleep(5)

# 从 f2 页面 跳转到默认页面
driver.switch_to.default_content()
driver.switch_to.frame("f1")

driver.find_element_by_link_text("click").click()

time.sleep(5)
driver.quit()
