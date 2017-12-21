from selenium import webdriver
driver = webdriver.PhantomJS(executable_path='C:/phantomjs/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.get("http://pythonscraping.com")
driver.implicitly_wait(1)
print(driver.get_cookies())
