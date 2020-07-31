
# coding = utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()

# driver.find_element_by_id("kw").send_keys("刘些宁")
# driver.find_element_by_id("su").click()
# time.sleep(3)
# # 清除对象内容
# driver.find_element_by_id("kw").clear()
# time.sleep(3)
# driver.find_element_by_id("kw").send_keys("柯南")
# driver.find_element_by_id("su").click()

# driver.find_element_by_id("kw").send_keys("刘些宁")
# driver.find_element_by_id("su").submit()

# text 用于获取元素的文本信息
# data = driver.find_element_by_xpath("//*[@id=\"s-bottom-layer-right\"]/span[1]").text
# print(data)   # 打印


time.sleep(6)
driver.quit()
