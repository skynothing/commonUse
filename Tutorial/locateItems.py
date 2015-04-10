# -*- coding: utf-8 -*-
'''
Created on 2015年3月31日

@author: root

Selenium提供了多种定位方法：
    id：最有效、最方便的方法
    name：跟id类似的
    class name：对某些具有相同类的元素一网打尽的好方法
    link text 和 partial link text： 用在定位超链接上比较多
    tag name：与class name有点类似
    css selector：如果你试用jQuery，这个一定是你
        使用在其父子元素间使用“ >”符号。
        WebElement userName = driver.findElement(By.cssSelector("form#loginForm > input"));
        
        使用“ +”操作符来定位兄弟元素。
        WebElement web = driver.findElement(By.cssSelector("#nv a + b"));
        
        下列表格列出了使用伪类来定位子元素癿例子：
            伪类                 例子                             描述
        :first-child     form#loginForm :first-child    定位表单里第一个子元素
        :last-child     form#loginForm :last-child    定位表单最后一个子元素
        :nth-child(2)     form#loginForm :nth-child(2)    定位表单中第二个子元素
        
        使用 UI 状态伪类，我们可以通过元素癿各种状态来定位，如 enabled,disable,checked。下例表格给予了详细癿说明
            伪类         例子             描述
        :enabled     input:enabled    定位所有属性为 enable input 元素
        :disabled     input:disabled    定位所有属性为 disabled input 元素
        :checked     input:checked    定位所有多选框 属性为checked 元素

定位到元素之后，就会有相应的动作
获取属性：get_attribute(self, name):  """Gets the given attribute or property of the element.
如：driver.find_element_by_id('stb').get_attribute('type')

输入字串：Simulates typing into the element. Use this to send simple key events or to fill out form fields:
如：driver.find_element_by_id('query').send_keys('abc')

清除文本内容：Clears the text if it's a text entry element.
如：driver.find_element_by_id('query').clear()

提交动作：submit(self): Submits a form. 
如：driver.find_element_by_id('stb')

获取CSS属性值：value_of_css_property(self, property_name):  """The value of a CSS property."""
如：driver.find_element_by_id('stb')

获取位置：@property    location(self):   """The location of the element in the renderable canvas."""
如：driver.find_element_by_id('stb')

获取大小：@property    size(self):     """The size of the element."""
如：driver.find_element_by_id('stb')

获取文本：@property    text(self):   The text of the element.
如：driver.find_element_by_id('stb')

获取tag标签类型： @property    tag_name(self):        """This element's ``tagName`` property."""
如：driver.find_element_by_id('stb')

是否可见：is_displayed(self):  """Whether the element is visible to a user."""
如：driver.find_element_by_id('stb')

是否处于可用：is_enabled(self):   """Returns whether the element is enabled."""
如：driver.find_element_by_id('stb')

是否被选中：is_selected(self):  """Returns whether the element is selected. Can be used to check if a checkbox or radio button is selected.  """
如：driver.find_element_by_id('stb')
'''


from selenium import webdriver
import time

driver = webdriver.Firefox()

# 打开搜狗网页
driver.get('http://www.sogou.com/')

# # 定位元素 by ID 
# driver.find_element_by_id('query').send_keys('test 1')
# driver.find_element_by_id('stb').click()
#  
# time.sleep(3)
# driver.get('http://www.sogou.com/')
#  
# # 定位元素 css
# # https://saucelabs.com/resources/selenium/css-selectors or http://www.360doc.com/content/13/1105/10/11675837_326750240.shtml for details
# driver.find_element_by_css_selector('input#query').send_keys('test 2')
# driver.find_element_by_css_selector('input#stb').click()
#  
# time.sleep(3)
# driver.get('http://www.sogou.com/')
#  
# # 定位元素 xpath
# driver.find_element_by_xpath("//input[@id='query']").send_keys('test 3')
# driver.find_element_by_xpath("//input[@id='stb']").click()
# time.sleep(3)
# driver.get('http://www.sogou.com/')
# 
# # 定位链接
# driver.find_element_by_link_text('新闻').click()
# time.sleep(2)
# driver.get('http://www.sogou.com/')
# driver.find_element_by_partial_link_text('新').click()

print 'attribute: %s' % driver.find_element_by_id('stb').get_attribute('type')
print 'css value: %s' % driver.find_element_by_id('stb').value_of_css_property('font-style')
print 'size: width %d / height %d' % (driver.find_element_by_id('stb').size['width'], driver.find_element_by_id('stb').size['height'])
print 'location: x %d / y %d' % (driver.find_element_by_id('stb').location['x'], driver.find_element_by_id('stb').location['y'])
print 'tag: ' + driver.find_element_by_id('stb').tag_name
print 'display: ' + driver.find_element_by_id('stb').is_displayed().__str__()
print 'enable: ' + driver.find_element_by_id('stb').is_enabled().__str__()
print 'selected: ' + driver.find_element_by_id('stb').is_selected().__str__()

driver.find_element_by_id('query').send_keys('clear me')
time.sleep(2)
driver.find_element_by_id('query').clear()


# 关闭当前浏览器窗口
time.sleep(3)
driver.close()