from selenium import webdriver
from Config import keys
import time

def fillForm():
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(keys['username'])
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(keys['password'])
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/button').click()
    driver.switch_to.frame("duo_iframe")
    driver.find_element_by_xpath('//*[@id="auth_methods"]/fieldset/div[1]/button').click()
    #driver.switch_to.frame(0)
    #driver.find_element_by_xpath('//*[@id="portal-navbar"]/ul/li[4]/a').click()
    

if __name__ == "__main__":
    driver = webdriver.Chrome('C:/Users/skim1/chromedriver_win32/chromedriver.exe')
    driver.get(keys['url'])
    fillForm()
    #driver.close()