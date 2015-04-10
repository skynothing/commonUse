# -*- coding: utf-8 -*-
'''
Created on 2015年3月31日

@author: root
'''

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://newtours.demoaut.com/')

print driver.title # TypeError: 'unicode' object is not callable: 一般是把字符串当做函数使用了。
driver.close()