"""Scrape books from a website using Selenium and BeautifulSoup."""
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
from settings import CATEGORIES

class ScrapBooks:
    """A class for scraping book data from a website."""
    # Disabling the "too many instance attributes" warning because eight is reasonable in this case.
    # pylint: disable=too-many-instance-attributes
    def __init__(self):
        """Create a new instance of the ScrapBooks class."""
        self.csv_filename = 'books.csv'
        self.site_books = []
        self.dataframe_books = None
        self.browser_obj = None
        self.book_obj = None

        # Browser and options objects
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.browser_obj = webdriver.Chrome(
            ChromeDriverManager().install(),
            chrome_options=self.options)

    def navigate_page(self, category_url):
        """Navigate to the specified category URL and scrape the page."""
        try:
            self.browser_obj.get(category_url)
            sleep(2)
            self.soup = BeautifulSoup(self.browser_obj.page_source, 'html.parser')
        except NameError as error:
            print(f"Erro initializing WebDriver: {error}")

    def fetch_books(self):
        """Scrapes the books from the website and saves the data to a CSV file."""
        try:
            sleep(3)
            books = self.soup.findAll(
                'li', attrs={'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'}
                )
            for book in books:
                # Book object with specific information
                self.book_obj = {
                    'name': book.find('h3').find('a', attrs={'title': True})['title'],
                    'category': self.soup.find('div', attrs={'class': 'page-header action'}).find('h1').text,
                    'stars': book.find('p', class_='star-rating')['class'][1],
                    'price': book.find('p', attrs={'class': 'price_color'}).text,
                    'is_stock': book.find('p', attrs={'class': 'instock availability'}).text.strip()
                }
                self.site_books.append(list(self.book_obj.values()))

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
        """Scrape all books from each category URL in CATEGORIES."""
        try:
            for category in CATEGORIES:
                self.navigate_page(category)
                self.fetch_books()
                print(f"Fetched books from category: {self.book_obj['category']}")
        except NameError as error:
            print(f"Erro initializing run function: {error}")


if __name__ == '__main__':
    scrap = ScrapBooks()
    scrap.run()
