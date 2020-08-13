
# coding = utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8080/20_07_14_blogdemo/login.html")
driver.maximize_window()

inputs = driver.find_elements_by_tag_name("input")

inputs[0].send_keys("123")
inputs[1].send_keys("123")
time.sleep(3)
inputs[2].click()
time.sleep(5)

driver.find_element_by_link_text("点击这里进行跳转").click()

index = driver.find_element_by_tag_name("form")

index.find_element_by_name("title").send_keys("title6")
index.find_element_by_name("content").send_keys("6666666666")
index.find_element_by_xpath("/html/body/form/input[2]").click()
time.sleep(4)
driver.find_element_by_link_text("点击这里进行跳转").click()

time.sleep(4)

# driver.find_element_by_xpath("/html/body/div[1]/a[2]").click()
divs = driver.find_element_by_tag_name("body").find_elements_by_tag_name("div")
divs[6].find_element_by_link_text("删除").click()
time.sleep(4)
driver.find_element_by_link_text("点击这里进行跳转").click()

time.sleep(4)

divs = driver.find_element_by_tag_name("body").find_elements_by_tag_name("div")
divs[0].find_element_by_link_text("title").click()


time.sleep(5)
driver.quit()

