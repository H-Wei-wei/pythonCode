
# 根据元素属性对元素进行定位

# coding = utf-8
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("https://www.baidu.com/")
time.sleep(6)

# 根据 id 来定位元素
# browser.find_element_by_id("kw").send_keys("selenium")
# browser.find_element_by_id("su").click()

# 根据 name 来定位元素
# browser.find_element_by_name("wd").send_keys("刘些宁")
# browser.find_element_by_id("su").click()

# 根据 class name 来定位元素
# browser.find_element_by_class_name("s_ipt").send_keys("刘些宁")
# browser.find_element_by_class_name("btn self-btn bg s_btn").click()

# 根据 link text （连接文本）来定位元素
# browser.find_element_by_link_text("高考加油").click()

# 根据 partial link text （部分连接文本）来定位元素
# browser.find_element_by_partial_link_text("高考").click()

# 根据 tag name （html标签的第一个元素）来定位元素
# browser.find_element_by_tag_name("input").send_keys("刘些宁")

# 根据 xpath 来定位
# browser.find_element_by_xpath("//*[@id=\"kw\"]").send_keys("刘些宁")
# browser.find_element_by_xpath("//*[@id=\"su\"]").click()

# 根据 css selector 来定位
browser.find_element_by_css_selector("#kw").send_keys("刘些宁")
browser.find_element_by_css_selector("#su").click()

time.sleep(6)
browser.quit()
