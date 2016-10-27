#coding=utf-8
from selenium import webdriver

'''
简易封装定位元素方法
'''

def findXP(driver,xpath):
    f = driver.find_element_by_xpath(xpath)
    return f

def findID(driver,id):
    f = driver.find_element_by_id(id)
    return f