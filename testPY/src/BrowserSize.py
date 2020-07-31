
# coding = utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 最大化页面
driver.maximize_window()
time.sleep(5)
# 最小化页面
driver.minimize_window()
time.sleep(5)

# 手动设置长宽
driver.set_window_size(200, 400)

time.sleep(6)
driver.quit()