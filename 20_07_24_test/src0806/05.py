
# 弹出框的处理

# coding = utf-8
from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
file_path = "file:///" + os.path.abspath("F:/Users/Administrator/Documents/selenium2html/alert.html#")
driver.get(file_path)
driver.maximize_window()

# 定位
driver.find_element_by_id("tooltip").click()
time.sleep(5)

# 得到弹出框的句柄
alert = driver.switch_to.alert

# 输出弹出框的内容
text = alert.text
print(text)

alert.accept()

time.sleep(3)
driver.quit()
