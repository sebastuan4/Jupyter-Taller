from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
class coca():
    #Definiendo variables
    def __init__(self):
        self.place="San Jose"
        self.chekIn="2022-07-23"
        self.chekOut="2022-07-28"
        self.noAdults=4
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
        
    def initialization(self):
        self.browser.get('https://www.booking.com/')
        self.browser.maximize_window()

    def setplace(self):
        search = self.browser.find_element(by=By.XPATH,value="//input[@id='ss']")
        search.send_keys(f"{self.place}")
        time.sleep(1)
        self.browser.find_element(by=By.XPATH,value='//li[@data-i="0"]').click()

    def date(self):
        self.browser.find_element(by=By.XPATH,value=f'//td[@data-date="{self.chekIn}"]').click()
        time.sleep(0.2)
        self.browser.find_element(by=By.XPATH,value=f'//td[@data-date="{self.chekOut}"]').click()

    def guests(self):
        self.browser.find_element(by=By.XPATH,value='//label[@id="xp__guests__toggle"]').click()
        for i in range(self.noAdults-2):
            self.browser.find_element(by=By.XPATH,value='//button[@aria-label="Increase number of Adults"]').click()

    def searchBtn(self):
        self.browser.find_element(by=By.XPATH,value='//button[@class="sb-searchbox__button "]').click()

    def deployment():
        v_ins=coca()
        v_ins.initialization()
        v_ins.setplace()
        time.sleep(1)
        v_ins.date()
        time.sleep(1)
        v_ins.guests()
        time.sleep(1)
        v_ins.searchBtn()
        time.sleep(20)
        
coca.deployment()
