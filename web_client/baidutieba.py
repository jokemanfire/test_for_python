# -*- coding:utf-8 -*-
import requests
import subprocess
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def deal():
    driver = webdriver.Firefox()
    driver.get("https://tieba.baidu.com/index.html")
    try:
        WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"登录")))
    finally:
        driver.find_element_by_link_text("登录").click()
    try:
        WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.NAME,"userName")))
    finally:
        driver.find_element_by_xpath('//input[@name="userName"]').clear()
        driver.find_element_by_xpath('//input[@name="userName"]').send_keys("hu981376433")
        driver.find_element_by_xpath('//input[@name="password"]').clear()
        driver.find_element_by_xpath('//input[@name="password"]').send_keys("hu123456") 
        driver.find_element_by_id('TANGRAM__PSP_8__submit').click() 
        time.sleep(3)  
    for i in driver.find_elements_by_class_name('unsign'):
        i.click()
    for handle in driver.window_handles: 
        driver.switch_to_window(handle)
        try:
            time.sleep(3)
            print(driver.title)
            driver.find_element_by_xpath('//a[@title="签到"]').click()
            driver.find_element_by_xpath('//a[@title="签到"]').click()
            driver.close()
        except:
            pass
        
if __name__ == "__main__":
    deal()
    
