#-*-coding:utf-8-*-  
from selenium import webdriver  
from selenium.webdriver.common.action_chains import ActionChains  
import time  
browser=webdriver.Firefox()  
browser.get("http://mail.163.com")
browser.switch_to_frame('x-URS-iframe')
browser.find_element_by_name("email").send_keys("17783350943")  
browser.find_element_by_name("password").send_keys("huding147852..")  
browser.find_element_by_id("dologin").click()  
browser.close()
