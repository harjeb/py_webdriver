# coding:utf-8
#import sys
#sys.path.append("\lib")
from lib import login
from selenium import webdriver

from selenium import webdriver
import os
import unittest
import configparser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from locator import HomeUI,WidgetUI
from lib import util
from selenium.webdriver.common.action_chains import ActionChains

#读取配置文件
configfile = os.path.abspath(os.path.join(os.path.dirname("__file__"),'config.ini'))
config = configparser.ConfigParser()
config.read(configfile)


class iu(unittest.TestCase):


    def test_create_dashboard(self):
        self.driver.find_element_by_xpath(HomeUI.Home.AddDashboardTab.WidgetSearch).send_keys(util.localstr('widgetTitle_ResourceList'))
        widget1 = self.driver.find_element_by_xpath(WidgetUI.Widget.Objectlist)
        ActionChains(self.driver).drag_and_drop_by_offset(widget1, 500, 500)











if __name__ == "__main__":
    unittest.main()