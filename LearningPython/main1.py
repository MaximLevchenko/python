from selenium import webdriver
from time import sleep
from selenium import webdriver







class InstaBot:

    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.instagram.com/?hl=ru')
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]") \
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
            .send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]') \
            .click()
        sleep(4)
        self.driver.find_element_by_xpath('//button[contains(text()."Не сейчас")]').click()


InstaBot('_max_leva_', '447781470659')
