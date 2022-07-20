from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
class webscraper():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get('https://www.w3schools.com/xml/xpath_examples.asp')
    browser.maximize_window()
    time.sleep(2)
    before = browser.find_element(by=By.XPATH,value='//a[@class="w3-left w3-btn"]')
    before2 = browser.find_element(by=By.XPATH,value='(//a[@class="w3-left w3-btn"])[1]')
    