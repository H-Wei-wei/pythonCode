
# 下拉框定位

# coding = utf-8
from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
file_path = "file:///" + os.path.abspath("F:/Users/Administrator/Documents/selenium2html/drop_down.html")
driver.get(file_path)
driver.maximize_window()

options = driver.find_elements_by_tag_name("option")

# for option in options:
#     if option.get_attribute("value") == "9.03":
#         option.click()

# 数组下标定位
options[3].click()

time.sleep(5)
driver.quit()


