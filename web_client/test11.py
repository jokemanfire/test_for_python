import requests
import subprocess
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def deal():
    driver = webdriver.PhantomJS(executable_path='C:/phantomjs/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    driver.get("https://www.baidu.com")
    driver.find_element_by_link_text("贴吧").click() 
    try:
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"登录")))
    finally:
        driver.find_element_by_link_text("登录").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//input[@name="userName"]').clear()
    driver.find_element_by_xpath('//input[@name="userName"]').send_keys("hu981376433")
    driver.find_element_by_xpath('//input[@name="password"]').clear()
    driver.find_element_by_xpath('//input[@name="password"]').send_keys("hu123456") 
    driver.find_element_by_id('TANGRAM__PSP_8__submit').click()  
    driver.implicitly_wait(10)
    for i in driver.find_elements_by_class_name('unsign'):
        i.click()
    for handle in driver.window_handles:
        driver.implicitly_wait(10)
        driver.switch_to_window(handle)
        try:
            print(driver.title)
            driver.find_element_by_xpath('//a[@title="签到"]').click()
            driver.find_element_by_xpath('//a[@title="签到"]').click()
            driver.close()
        except:
            pass
    
   
        
if __name__ == "__main__":
    deal()
    
