import os
import os.path
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def setup():
    configFile = open('Config.txt', 'w+')
    
    def getUsername():
        print('Enter your username:')
        usr = input()
        print('Is ' + usr + ' correct? <Y:N>')
        confirm = input()
        if (confirm == 'Y'):
            configFile.write(usr + '\n')
        else:
            getUsername()
  
    def getPassword():
        print('Enter your password:')
        pwd = input()
        print('Is ' + pwd + ' correct? <Y:N>')
        confirm = input()
        if (confirm == 'Y'):
            configFile.write(pwd + '\n')
        else:
            getPassword()
    
    getUsername()
    getPassword()
    configFile.close()


def fillForm():
    configFile = open('Config.txt', 'r')
    username = configFile.readline().rstrip('\n')
    password = configFile.readline().rstrip('\n')

    driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="userInput"]/form/button').click()
    driver.get('https://dailyhealth.rit.edu/assessment')
    
    
    

if __name__ == "__main__":
    if not os.path.exists('./Config.txt'):
        setup()
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://dailyhealth.rit.edu/')
    fillForm()
    time.sleep(10)
    #driver.close()