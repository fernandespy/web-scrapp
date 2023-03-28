"""Imports"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('http://books.toscrape.com/')
sleep(3)

def navegation_page():
    """Navigate through pages"""
    page_content = driver.page_source
    site = BeautifulSoup(page_content, 'html.parser')
    books = site.find_element('xpath', '//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[1]')
    print(books.prettify())
#navegation_page()
