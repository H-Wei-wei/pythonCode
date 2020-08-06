
# 层级定位

# coding = utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import os
driver = webdriver.Chrome()
file_path = "file:///" + os.path.abspath("F:/Users/Administrator/Documents/selenium2html/level_locate.html#")
driver.get(file_path)
driver.maximize_window()

# 定位到 link1
driver.find_element_by_link_text("Link1").click()
time.sleep(3)
# 定位需要鼠标移动到目标元素
index = driver.find_element_by_link_text("Another action")
# 将鼠标移动到目标元素
ActionChains(driver).move_to_element(index).perform()

time.sleep(10)
driver.quit()
