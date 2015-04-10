# -*- coding: utf-8 -*-
'''
Created on 2015年3月31日

@author: root
'''
from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Firefox()


# 
# numbers = driver.find_elements_by_css_selector('ol > li')
# 
# for one in numbers:
#     one.click()
#     time.sleep(0.1)

""" 

# move_to_element_with_offset & move_by_offset 没成功过

driver.get('file:///root/HTML/Selectable.html')
one = driver.find_element_by_css_selector("li[name='one']")
X = one.location['x']
Y = one.location['y']
Width = one.size['width']
Height = one.size['height']
print 'x:%d, y:%d, width:%d, height:%d'%(X,Y,Width,Height)
action = ActionChains(driver)
action.move_to_element_with_offset(one,X+Width+1, Y+1).click().perform()
"""

''' 
file:///root/HTML/ContextClick.html#
'''
driver.get('file:///root/HTML/ContextClick.html')

one = driver.find_element_by_css_selector("li[name='one']")

#close browser
time.sleep(2)
driver.close()