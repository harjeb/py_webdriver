#coding=utf-8
import os
import configparser

configfile = os.path.abspath(os.path.join(os.path.dirname("__file__"),'c:\Code\config.ini'))
config = configparser.ConfigParser()
config.read(configfile)
resourcelocator = 'c:\Code\Resources\%s_resources.ini' %(config['vrops']['testlanguage'])
lang = config['vrops']['testlanguage']
resourcefile = os.path.abspath(os.path.join(os.path.dirname("__file__"),resourcelocator))
#encoding指定解码格式
config.read(resourcefile,encoding="utf8")

def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except FileNotFoundError: return False
    return True

'''
调用本地化字符串函数
example:  localstr('chrome.about')   will output 'about'
'''
def localstr(str):
     return config[lang][str]

