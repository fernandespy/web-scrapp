"""Imports"""
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

class ScrapBooks:
    """Scrap books from page"""
    def __init__(self):
        self.csv_filename = 'books.csv'
        self.categories =  [
        'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html',
        'http://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html'
    ]
        self.url_path = "http://books.toscrape.com/"
        self.site_books = []
        self.df_books = None
        self.browser = None
        self.next_page = None
        self.soup = None
        self.books = None
        self.books_name = None
        self.books_category = None
        self.books_stars = None
        self.books_price = None
        self.books_is_stock = None

    def navegate_page(self, category_url):
        """Navegate to pages"""
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get(category_url)
        sleep(2)
        self.soup = BeautifulSoup(self.browser.page_source, 'html.parser')

    def fetch_books(self):
        """Fetch books from page"""
        sleep(3)
        self.books = self.soup.findAll('li', attrs={'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
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
            self.df_books = pd.DataFrame(self.site_books, columns=[
                'Book Name',
                'Book Category',
                'Book Star Rating',
                'Book Price',
                'Book in Stock'])
            self.df_books.to_csv(self.csv_filename, index=False)
            
    def run(self):
        """Fetch all books from categories urls list"""
        for category in self.categories:
            self.navegate_page(category)
            self.fetch_books()


if __name__ == '__main__':
    scrap = ScrapBooks()
    scrap.run()
