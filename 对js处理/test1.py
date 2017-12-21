from selenium import webdriver
import time
from urllib.request import urlopen

driver = webdriver.PhantomJS(executable_path='C:/phantomjs/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
print(driver.find_element_by_id('content').text)
driver.close()
ff = urlopen("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
print(ff.read())
