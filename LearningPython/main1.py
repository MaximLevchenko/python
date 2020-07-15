from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span').click()
        sleep(2)

        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        sleep(4)

    def open_chat(self):
        self.driver.find_element_by_link_text("net_tale").click()  # Clicking on specific person
        sleep(2)
        dms_box = self.driver.find_element_by_xpath('//textarea[@placeholder="Напишите сообщение..."]')
        dms_box.send_keys('Test', '\ue007')


my_bot = InstaBot('_max_leva_', '447781470659maks')
