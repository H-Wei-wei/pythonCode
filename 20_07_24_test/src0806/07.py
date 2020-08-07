
# 上传文件

# coding = utf-8
from selenium import webdriver
import time
import os
file_path = "file:///" + os.path.abspath("F:/Users/Administrator/Documents/selenium2html/upload.html")
driver = webdriver.Chrome()
driver.get(file_path)

# 定位到上传文件框
driver.find_element_by_tag_name("input").send_keys("F:/Users/Administrator/Documents/selenium2html/upload.html")

time.sleep(5)
driver.quit()
