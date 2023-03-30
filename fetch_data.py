"""Imports"""
from time import sleep
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

## Setup chrome options
chrome_options = Options()
#chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--disable-dev-shm-usage')

service = Service(executable_path=ChromeDriverManager().install())
#homedir = os.path.expanduser("~")
#webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

browser = webdriver.Chrome(service=service, options=chrome_options)
browser.get('http://books.toscrape.com/')
sleep(3)

def navegation_page():
    """Navigate through pages"""
    page_content = browser.page_source
    site = BeautifulSoup(page_content, 'html.parser')
    books = site.find('li', "product_pod")
    print(books.prettify())
#navegation_page()

print('done')