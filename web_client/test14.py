from selenium import webdriver
from bs4 import BeautifulSoup
import Requests

driver = webdriver.Firefox()
driver.get('https://passport.baidu.com/v2/?login')
dirver.switch_to_frame('TANGRAM__PSP_3__form')
driver.find_element_by_name('userName').clear()
driver.find_element_by_name('userName').send_keys("hu981376433")
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys("hu123456") 
driver.find_element_by_id('TANGRAM__PSP_3__submit').click() 
 