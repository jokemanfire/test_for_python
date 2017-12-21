import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver

#创建显得selenium driver
driver = webdriver.PhantomJS(executable_path='C:/phantomjs/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.get("http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
time.sleep(2)
#单击图书预览按钮
driver.find_element_by_id("sitbLogoImg").click()
imageList = set()
#等待页面加载完成
time.sleep(5)
#当向右箭头可以点击时翻页
while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    time.sleep(2)
    #获取新加载的页面
    pages = driver.find_element_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        image = page.get_attribute("src")
        imageList.add(image)

driver.quit()
#用Tesseract处理我们收集到的图片URL
for image in sorted(imageList):
    urlretrieve(image,"page.jpg")
    p = subprocess.Popen(["tesseract","page.jpg","page"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    p.wait()
    f = open("page.txt","r")
    print(f.read())