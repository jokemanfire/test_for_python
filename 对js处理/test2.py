from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

dirver = webdriver.PhantomJS(executable_path='C:/phantomjs/phantomjs-2.1.1-windows/bin/phantomjs.exe')
dirver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
try:
    element = WebDiverWait(driver,10).until(EC.presence_of_element_located((By.ID,"loadedButton")))
finally:
    print(driver.find_element_by_id("content").text)
    driver.close()
