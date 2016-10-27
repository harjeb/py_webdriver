# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time
import os
import configparser
#import sys
#sys.path.append("\package")
from package import location
import datetime


#读取配置文件
configfile = os.path.abspath(os.path.join(os.path.dirname("__file__"),'config.ini'))
config = configparser.ConfigParser()
config.read(configfile)


#调用location.py文件的定位方法
lo = location



class Login(unittest.TestCase):

    def runTest(self):
        assert(True == True)


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = config['vrops']['server']
        self.verificationErrors = []
        self.accept_next_alert = True

        #vrops 登陆用例
    def test_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.set_window_size(1280, 1024)
        driver.get(self.base_url + "/ui")

        #登陆
        driver.find_element_by_xpath("//input[@id='userName-inputEl']").send_keys(config['vrops']['username'])
        driver.find_element_by_xpath("//input[@id='password-inputEl']").send_keys(config['vrops']['password'])
        driver.find_element_by_xpath("//a[@id='loginBtn']").click()
        #driver.find_element_by_id("loginBtn-btnEl").click()



        try:
            driver.implicitly_wait(15)
            lo.findID("objectNavigatorToolbarHomeBtn-btnWrap")
        except:
            driver.get_screenshot_as_file('C:\code\pic\errorlogin%s.png' %time.strftime("%Y%m%d.%H%M%S"))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == "__main__":
    unittest.main()