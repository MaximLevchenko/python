from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self,username,pw):
        self.driver=webdriver.Chrome()
        self.driver.get('https://www.instagram.com/?hl=ru')
        sleep(2)

InstaBot('_max_leva_','447781470659')
