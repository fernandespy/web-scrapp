# pylint: disable=too-few-public-methods
"""Imports"""
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


class ScrapBooks:
    """Scrap books from page"""
    def __init__(self):
        self.url_path = "http://books.toscrape.com/"
        self.site_books = {}
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get(self.url_path)
        self.soup = BeautifulSoup(self.browser.page_source, 'html')
        self.books = None

    def fetch_books(self):
        """Fetch books from page"""
        sleep(3)
        self.books = self.soup.find('li', attrs={'class':'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
        print(self.books.prettify())


scrap = ScrapBooks()
scrap.fetch_books()
