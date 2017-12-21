from selenium import webdriver
import time 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from bs4 import BeautifulSoup
import subprocess
from urllib.request import urlretrieve

def sublinme(url):
    driver = webdriver.Firefox()
    driver.get(url)
    driver.find_element_by_link_text("登录").click()
    time.sleep(3)
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys("17783350943")
    driver.find_element_by_name("password")
    driver.find_element_by_name("password").send_keys("a123456")
    image = driver.find_element_by_id("reloadimg")
    txt = image(image)
    driver.find_element_by_id("rand").send_keys(txt)
    driver.find_element_by_link_text("登录").click()
    time.sleep(2)
    driver.find_element_by_link_text("个人中心").click()
    try:
        WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.NAME,"重庆邮电大学(02111607)")))
    finally:
        driver.find_element_by_xpath('//a[@href="study_index.htm"]').click()
    try:
        WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.CLASS_NAME,"/wk/index.htm?id=40")))
    finally:
        driver.find_element_by_xpath('//a[@span="进入学习"]').click()
    windows = driver.window_handles
    driver.switch_to_window(windows[1])
    time.sleep(2)
    driver.find_element_by_link_text("课程学习")
    time.sleep(2)
    for i in range(831,850):
        link =  str("//a[@href=\"learn.htm?id=40&jid=""")+ str(i)+ "]" + "\""
        driver.find_element_by_xpath(link).click()
        html(driver.page_source)
        meicai = driver.find_elements_by_xpath('//[@span="马上评价"')
        for k in meicai:
            k.click()
            time.sleep(2)
            k.find_element_by_xpath('//input[@class="ping_btn_2"]').click()
            time.sleep(2)
            k.find_element_by_xpath('//button[@class="aui_state_highlight"]').click()
            time.sleep(2)
            k.find_element_by_link_text("×").click()
            time.sleep(5)


 
def image(image):
    urlretrieve(image,"pa.jpg")
    p = subprocess.Popen(["tesseract","pa.jpg","page"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    p.wait()
    f = open("page.txt","r")
    return (f.read())


def html(htm):
    page1 = BeautifulSoup(htm)
    try:
        tim = page1.findAll('span',title="学习时间").get_text()
        time.sleep(tim)
    except:
        pass

def main(url):
    sublinme(url)


if __name__ == '__main__':
    url = 'http://www.attop.com/index.htm'
    main(url)
