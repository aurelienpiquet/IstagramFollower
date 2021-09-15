from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import re

chrome_driver_path = "../chromedriver.exe"


url = 'https://www.instagram.com/'
istagram_account = 'xxxx'
istagram_password = 'xxxx'

class InstaFollower:
    def __init__(self):        
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)       
        self.driver.get(url)
        sleep(1)

    def login(self):
        btn_cookie = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
        btn_cookie.click()
        sleep(1)
        user = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        user.send_keys(istagram_account)
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(istagram_password)
        connexion = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        connexion.click()
        sleep(3)

    def find_followers(self, toFollow):
        self.driver.get(url + toFollow)
        sleep(1)
        btn_follower = self.driver.find_element_by_css_selector("ul li a")
        btn_follower.click()
        sleep(2)
        scr1 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(2):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
            sleep(2)

    def follow(self):
        liste_followers = self.driver.find_elements_by_css_selector('ul div li div div button')
        for follower in liste_followers:
            print(follower.name)
            if re.search(r"abonner", str(follower.text)):
                follower.click()
                sleep(0.5)
                print("On click")
 

if __name__ == "__main__":
    bot = InstaFollower()
    bot.login()
    bot.find_followers("chef.etchebest")
    bot.follow()