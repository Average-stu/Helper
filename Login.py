from selenium import webdriver
from time import sleep
from account_details import G_password , G_username , Insta_password, Insta_username
from selenium.webdriver.common.keys import Keys
from random import randint

class login:
    def __init__(self, G_username, G_password,Insta_username,Insta_password):
        self.G_username = G_username
        self.G_password = G_password
        self.Insta_username = Insta_username
        self.Insta_password = Insta_password

    def G_login(self):
        self.bot = webdriver.Firefox()
        bot = self.bot
        print("\nStarting Login process!\n")
        bot.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27') # for log-in process
        bot.implicitly_wait(10)
        self.bot.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        self.bot.find_element_by_xpath('//input[@type="email"]').send_keys(self.G_username)
        self.bot.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.bot.find_element_by_xpath('//input[@type="password"]').send_keys(self.G_password)
        self.bot.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
        self.bot.get('https://www.gmail.com') # The url of the Youtube channel

    def Insta_login(self):
        self.bot = webdriver.Firefox()
        bot = self.bot
        print("Instagram")
        self.bot.get('https://www.instagram.com/accounts/login')
        bot.implicitly_wait(10)
        self.bot.find_element_by_name('username').send_keys(self.Insta_username)
        self.bot.find_element_by_name('password').send_keys(self.Insta_password)
        submit = self.bot.find_element_by_tag_name('form')
        submit.submit()
        bot.implicitly_wait(200)
        notifications = self.bot.find_element_by_tag_name('button')
        notifications.click()
        print("\nLoggedin Successfully!\n")




