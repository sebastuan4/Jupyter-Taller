from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
class webscraper():
    #Definiendo variables
    def __init__(self):
        self.place="San Jose"
        self.chekIn="2022-07-21"
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
        p=webscraper()
        p.initialization()
        p.setplace()
        time.sleep(1)
        p.date()
        time.sleep(1)
        p.guests()
        time.sleep(1)
        p.searchBtn()
        time.sleep(20)
        
webscraper.deployment()
    









"""
search = browser.find_element(by=By.XPATH,value="//input[@id='ss']")
search.send_keys("San Jose")
time.sleep(1)
browser.find_element(by=By.XPATH,value='//li[@data-i="0"]').click()
browser.find_element(by=By.XPATH,value=f'//td[@data-date="{checkIn}"]')
"""    

    
