from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from secrets import pw





class InstaBot:

    def __init__(self, username, password):
        self.username = username;
        self.driver = webdriver.Chrome()

        self.driver.get('https://www.instagram.com/?hl=ru')
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]") \
            .send_keys(username)#Process of logining in(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
            .send_keys(password) #Process of logining in(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]') \
            .click() #Submitting our log in form
        sleep(4)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div/div/div/button').click()  # Notifications
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()  # Notifications
        sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span').click()  # Profile
        sleep(2)

        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div').click()  # Profile
        sleep(2)
        followers = self.followers()

    def followers(self):
        sleep(2)
        self.driver.find_element_by_xpath('//a[@href="/_max_leva_/followers/"]').click()  # Followers list

        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")  # Scrolling body
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""   
                        arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                        return arguments[0].scrollHeight;
                        """, scroll_box)
            # Scrolling the end of the scrolling block
        links = scroll_box.find_elements_by_tag_name('a') # Getting all user names with tag 'a'
        names = [name.text for name in links if
                 name.text != '']  # We are making a for loop for links and checking whether or not thee
        sorted_names=sorted(names)
        print(sorted_names)
        return sorted_names

    # self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div[2]/button") \
    # .click()
    # return names
    # self.driver.find_element_by_xpath('//a[@href="/net tale/"]').click()
    # sleep(3)
    # sugs=self.driver.find_element_by_xpath()

    # self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
    # sleep(4) #Getting into dms

    def open_chat(self):
        self.driver.find_element_by_link_text("net_tale").click()  # Clicking on specific person
        sleep(2)
        dms_box = self.driver.find_element_by_xpath('//textarea[@placeholder="Напишите сообщение..."]')
        dms_box.send_keys('Test', '\ue007')


my_bot = InstaBot('_max_leva_', '447781470659maks')
