from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

class InstagramBot:
    def __init__(self, username, password ):
        self.username = username
        self.password = password

    
        self.driver = webdriver.Chrome('./chromedriver.exe')

        self.login()

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        time.sleep(4)
        
    def target_id(self,userid):
        self.userid = userid
        self.driver.get('https://www.instagram.com/' + self.userid)



    def likepics(self, amount):
        self.amount = amount
        self.driver.find_element_by_class_name('v1Nh3').click()  #clicks the first picture

        i = 1
        while i <= amount:
            time.sleep(3)
            self.driver.find_element_by_class_name('fr66n').click()    #like button
            time.sleep(2)
            self.driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()   #next button
            time.sleep(1)
            i += 1
        self.driver.get('https://www.instagram.com/' + self.username)



ig_bot = InstagramBot('PLEASE ENTER THE USER ID','PLEASE ENTER THE PASSWORD',)  # if i dont give '  ig_bot ' chrome browser crashes
ig_bot.target_id('PLEASE ENTER THE TARGET USER ID')
ig_bot.likepics(ENTER THE AMOOUNT OF PICTURES )  #enter the number of pictures that you want to like

    
