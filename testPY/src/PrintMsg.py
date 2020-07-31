
# coding = utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()

# 打印 title
print("title：" + driver.title)
# 打印 url
print("url：" + driver.current_url)

time.sleep(6)
driver.quit()
