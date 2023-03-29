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
            "http://books.toscrape.com/catalogue/category/books/travel_2/index.html",
            "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
            "http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html",
            "http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html",
            "http://books.toscrape.com/catalogue/category/books/classics_6/index.html",
            "http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html",
            "http://books.toscrape.com/catalogue/category/books/romance_8/index.html",
            "http://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html",
            "http://books.toscrape.com/catalogue/category/books/fiction_10/index.html",
            "http://books.toscrape.com/catalogue/category/books/childrens_11/index.html",
            "http://books.toscrape.com/catalogue/category/books/religion_12/index.html",
            "http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html",
            "http://books.toscrape.com/catalogue/category/books/music_14/index.html",
            "http://books.toscrape.com/catalogue/category/books/default_15/index.html",
            "http://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html",
            "http://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html",
            "http://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html",
            "http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html",
            "http://books.toscrape.com/catalogue/category/books/new-adult_20/index.html",
            "http://books.toscrape.com/catalogue/category/books/young-adult_21/index.html",
            "http://books.toscrape.com/catalogue/category/books/science_22/index.html",
            "http://books.toscrape.com/catalogue/category/books/poetry_23/index.html",
            "http://books.toscrape.com/catalogue/category/books/paranormal_24/index.html",
            "http://books.toscrape.com/catalogue/category/books/art_25/index.html",
            "http://books.toscrape.com/catalogue/category/books/psychology_26/index.html",
            "http://books.toscrape.com/catalogue/category/books/autobiography_27/index.html",
            "http://books.toscrape.com/catalogue/category/books/parenting_28/index.html",
            "http://books.toscrape.com/catalogue/category/books/adult-fiction_29/index.html",
            "http://books.toscrape.com/catalogue/category/books/humor_30/index.html",
            "http://books.toscrape.com/catalogue/category/books/horror_31/index.html",
            "http://books.toscrape.com/catalogue/category/books/history_32/index.html",
            "http://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html",
            "http://books.toscrape.com/catalogue/category/books/christian-fiction_34/index.html",
            "http://books.toscrape.com/catalogue/category/books/business_35/index.html",
            "http://books.toscrape.com/catalogue/category/books/biography_36/index.html",
            "http://books.toscrape.com/catalogue/category/books/thriller_37/index.html",
            "http://books.toscrape.com/catalogue/category/books/contemporary_38/index.html",
            "http://books.toscrape.com/catalogue/category/books/spirituality_39/index.html",
            "http://books.toscrape.com/catalogue/category/books/academic_40/index.html",
            "http://books.toscrape.com/catalogue/category/books/self-help_41/index.html",
            "http://books.toscrape.com/catalogue/category/books/historical_42/index.html",
            "http://books.toscrape.com/catalogue/category/books/christian_43/index.html",
            "http://books.toscrape.com/catalogue/category/books/suspense_44/index.html",
            "http://books.toscrape.com/catalogue/category/books/short-stories_45/index.html",
            "http://books.toscrape.com/catalogue/category/books/novels_46/index.html",
            "http://books.toscrape.com/catalogue/category/books/health_47/index.html",
            "http://books.toscrape.com/catalogue/category/books/politics_48/index.html",
            "http://books.toscrape.com/catalogue/category/books/cultural_49/index.html",
            "http://books.toscrape.com/catalogue/category/books/erotica_50/index.html",
            "http://books.toscrape.com/catalogue/category/books/crime_51/index.html"
        ]
        self.url_path = "http://books.toscrape.com/"
        self.site_books = []
        self.dataframe_books = None
        self.browser = None
        self.options = None
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
            for category in self.categories:
                self.navegate_page(category)
                self.fetch_books()
                print(f"Fetch Books: {self.books_category}")
        except NameError as error:
            print(f"Erro initializing run function: {error}")


if __name__ == '__main__':
    scrap = ScrapBooks()
    scrap.run()
