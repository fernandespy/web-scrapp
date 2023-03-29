"""Imports"""
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
from settings import CATEGORIES

class ScrapBooks:
    """Scrap books from page"""
    # pylint: disable=too-many-instance-attributes
    # Eight is reasonable in this case.
    def __init__(self):
        self.csv_filename = 'books.csv'
        self.site_books = []
        self.dataframe_books = None
        self.browser = None
        self.options = None
        self.soup = None
        self.books = None
        self.books_name = None
        self.books_category = None
        self.books_stars = None
        self.books_price = None
        self.books_is_stock = None

    def navegate_page(self, category_url):
        """Navegate to pages"""
        try:
            self.options = webdriver.ChromeOptions()
            self.options.add_argument("--headless")
            self.browser = webdriver.Chrome(
                ChromeDriverManager().install(),
                chrome_options=self.options)
            self.browser.get(category_url)
            sleep(2)
            self.soup = BeautifulSoup(self.browser.page_source, 'html.parser')
        except NameError as error:
            print(f"Erro initializing WebDriver: {error}")

    def fetch_books(self):
        """Fetch books from page"""
        try:
            sleep(3)
            self.books = self.soup.findAll(
                'li', attrs={'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'}
                )
            for book in self.books:
                # name of book
                self.books_name = book.find('h3').find('a', attrs={'title': True})
                self.books_name = self.books_name['title']

                # category of book
                self.books_category = self.soup.find(
                    'div', attrs={'class': 'page-header action'}).find('h1')
                self.books_category = self.books_category.text

                # stars of book
                self.books_stars = book.find('p', class_='star-rating')
                self.books_stars = self.books_stars['class'][1]

                # price of book
                self.books_price = book.find('p', attrs={'class': 'price_color'})
                self.books_price = self.books_price.text

                # availability of book
                self.books_is_stock = book.find('p', attrs={'class': 'instock availability'})
                self.books_is_stock = self.books_is_stock.text.strip()

                self.site_books.append(
                    [self.books_name,
                    self.books_category,
                    self.books_stars,
                    self.books_price,
                    self.books_is_stock])
                self.dataframe_books = pd.DataFrame(self.site_books, columns=[
                    'Book Name',
                    'Book Category',
                    'Book Star Rating',
                    'Book Price',
                    'Book in Stock'])
                self.dataframe_books.to_csv(self.csv_filename, index=False)
        except NameError as error:
            print(f"Erro initializing fetch_books: {error}")

    def run(self):
        """Fetch all books from categories urls list"""
        try:
            for category in CATEGORIES:
                self.navegate_page(category)
                self.fetch_books()
                print(f"Fetch Books: {self.books_category}")
        except NameError as error:
            print(f"Erro initializing run function: {error}")


if __name__ == '__main__':
    scrap = ScrapBooks()
    scrap.run()
