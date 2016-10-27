# coding:utf-8

from selenium import webdriver
import os
import unittest
import configparser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from locator import HomeUI

#读取配置文件
configfile = os.path.abspath(os.path.join(os.path.dirname("__file__"),'config.ini'))
config = configparser.ConfigParser()
config.read(configfile)


class ui(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = config['vrops']['server']
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.maximize_window()
        self.driver.set_window_size(1280, 1024)
        self.driver.get(self.base_url + "/ui")
        # 登陆
        self.driver.find_element_by_xpath("//input[@id='userName-inputEl']").send_keys(config['vrops']['username'])
        self.driver.find_element_by_xpath("//input[@id='password-inputEl']").send_keys(config['vrops']['password'])
        self.driver.find_element_by_xpath("//a[@id='loginBtn']").click()
        time.sleep(15)

    def test_create_newdashboard(self):

        try:
            self.driver.implicitly_wait(15)
            self.driver.find_element_by_id("objectNavigatorToolbarHomeBtn-btnWrap")

        except:
            self.driver.get_screenshot_as_file('C:\code\pic\errorlogin%s.png' %time.strftime("%Y%m%d.%H%M%S"))
            print("login error")

        try:
            WebDriverWait(self.driver, 15, 1).until(EC.element_to_be_clickable((By.ID,"objectNavigatorToolbarHomeBtn-btnWrap")))
        finally:
            self.driver.find_element_by_xpath(HomeUI.Home.btn_actions).click()
            self.driver.find_element_by_xpath(HomeUI.Home.create_dashboard_action).click()
            self.driver.find_element_by_xpath()












if __name__ == "__main__":
    unittest.main()