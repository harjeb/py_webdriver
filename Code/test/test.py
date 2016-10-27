# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

#filepath = 'file:///' + os.path.abspath('checkout.html')
vrops = 'http://172.16.186.72/ui'
driver = webdriver.Firefox()
#driver.get(filepath)
driver.get(vrops)
time.sleep(3)
driver.set_window_size(1280, 1024)
#driver.find_element_by_xpath("//input[@id='c3']").click()
driver.find_element_by_xpath("//input[@id='userName-inputEl']").send_keys("admin")
driver.find_element_by_xpath("//input[@id='password-inputEl']").send_keys("@WSX3edc")
