# selenium框架实现打开百度并搜索功能
from selenium import webdriver
import time
# 初始化
driver=webdriver.Chrome(chrome_options={})
driver.get('https://www.baidu.com')

input=driver.find_element_by_css_selector('.s_ipt')
button=driver.find_element_by_css_selector('#su')
input.send_keys("进击的巨人")
time.sleep(3)
button.click()
input.clear()
input.send_keys('泽野弘之')