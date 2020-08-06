
# 定位一组元素

# coding=utf-8
from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
file_path = "file:///" + os.path.abspath("F:/Users/Administrator/Documents/selenium2html/checkbox.html")
driver.get(file_path)
driver.maximize_window()

# 定位一组元素
inputs = driver.find_elements_by_tag_name("input")

# for input in inputs:
#     if input.get_attribute("type") == "checkbox":
#         input.click()

for input in inputs:
    if input.get_attribute("type") == "radio":
        input.click()

# driver.find_element_by_id("c1").click()
time.sleep(5)

driver.quit()
