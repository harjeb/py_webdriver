#coding=utf-8
import os
import configparser

#读取配置文件
configfile = os.path.abspath(os.path.join(os.path.dirname("__file__"),'c:\Code\config.ini'))
config = configparser.ConfigParser()
config.read(configfile)
resourcelocator = 'c:\Code\Resources\%s_resources.ini' %(config['vrops']['testlanguage'])
lang = config['vrops']['testlanguage']
resourcefile = os.path.abspath(os.path.join(os.path.dirname("__file__"),resourcelocator))
#encoding指定解码格式
config.read(resourcefile,encoding="utf8")

class Widget():
    Objectlist = "//img[@key='ResourceList']"