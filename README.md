# Scraping Books from a Website

This is a Python script that uses Selenium and BeautifulSoup to scrape book data from a website and save it to a CSV file.

## Requirements

To run this script, you will need:

- Python 3.x
- `selenium`: to automate the browser and make requests to the web page
- `beautifulsoup4`: for parsing and extracting the HTML data.
- `pandas`: to save the collected data to a CSV file.
- ChromeDriver (automatically downloaded by `webdriver_manager`)

## How to use

1. Clone the repository: `git clone https://github.com/fernandespy/web-scrapp.git`.
2. Install the required packages by running `pip install -r requirements.txt` in the project directory.
3. Modify the `CATEGORIES` list in `settings.py` to include the URLs of the categories you want to scrape.
4. Run `python scrape_books.py` in the project directory to scrape the books.

## Files

- `scrape_books.py`: The main script that contains the functions for navigating the page and extracting information from the books.
- `settings.py`: A file containing the URLs of the book categories to be collected.
- `requirements.txt`: A text file containing the Python dependencies needed to run the script.

## License

This project is licensed under the MIT License. See `LICENSE` for more information.