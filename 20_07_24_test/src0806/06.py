
# div 对话框的处理

# coding = utf-8
from selenium import webdriver
import time
import os
driver = webdriver.Firefox()
file_path = "file:///" + os.path.abspath("F:/Users/Administrator/Documents/selenium2html/modal.html#")
driver.get(file_path)
driver.maximize_window()

# 点击 Click
driver.find_element_by_link_text("Click").click()

# 定位 div
div1 = driver.find_element_by_class_name("modal-body")
driver.implicitly_wait(5)
# 点击 click me
div1.find_element_by_link_text("click me").click()

time.sleep(5)

# 关闭弹出框
# 1.定位 div
div2 = driver.find_element_by_class_name("modal-footer")
# 2.点击关闭按键
buttons = div2.find_elements_by_tag_name("button")
buttons[0].click()

time.sleep(5)
driver.quit()

