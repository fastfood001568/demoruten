#-*coding:utf-8-*
from  selenium import webdriver
import time


driver=webdriver.Chrome()
driver.get('https://www.ruten.com.tw/')
driver.maximize_window()   
element=driver.find_element_by_id('keyword').send_keys('iphone11')
time.sleep(1)
driver.find_element_by_class_name('rt-header-search-submit').click()
driver.save_screenshot('searchitems.png')
driver.quit()
