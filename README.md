# Scraping and Saving Book Data with Python and PostgreSQL

This project demonstrates how to use Python to scrape book data from a website and save it to a CSV file. It also includes a script for connecting to a PostgreSQL database and inserting the scraped data into a table. By following the steps outlined in this README, you will be able to collect and store book data in a structured format for further analysis.

## Website Information

This script is designed to scrape book data from http://books.toscrape.com/. The website contains information on a wide variety of books, including title, author, publication date, genre, and more.
The site was made precisely to be scraped! So all information obtained is for public use and anyone is free to use the site!!

## Requirements

To run this project, you will need the following software packages and dependencies:

- Python 3.x
- `selenium`: to automate the browser and make requests to the web page
- `beautifulsoup4`: for parsing and extracting the HTML data.
- `pandas`: to save the collected data to a CSV file.
- ``psycopg2``: for connecting to PostgreSQL database and executing SQL queries.
- ``dotenv``: for loading the environment variables from a ``.env`` file.
- ChromeDriver (automatically downloaded by ``webdriver_manager``)"

## How to use

To use this project, follow these steps:

1. Clone the repository: `git clone https://github.com/fernandespy/web-scrapp.git`.
2. Install the required packages by running `pip install -r requirements.txt` in the project directory.
3. Modify the `CATEGORIES` list in `settings.py` to include the URLs of the categories you want to scrape. To add a new category, simply copy the format of the existing URLs and replace the category name and URL with your own.
4. Run `scrape_books.py` in the project directory to scrape the books. The script will save the data to a CSV file named books.csv in the project directory.
5. Create a ``.env`` file and add the constants:
`DB_HOST='yourhost', DB_NAME='yourdbname', DB_USER='yourdbuser', DB_PASSWORD='yourdbpassword', DB_PORT='yourdbport'`.
6. Run ``db_manager.py`` in the project directory to save the data to PostgreSQL."

## Files

- `scrape_books.py`: The main script that contains the functions for navigating the page and extracting information from the books.
- `settings.py`: A file containing the URLs of the book categories to be collected.
- `requirements.txt`: A text file containing the Python dependencies needed to run the script.
- ``db_manager.py``: 
The main script that contains the functions for connecting to the PostgreSQL database, creating a table and inserting data from the CSV file.
- ``books.csv``: A CSV file containing the book data that will be inserted into the database.
- ``.env``: A file containing the environment variables for connecting to the PostgreSQL database.


## Comments

I used a postgres database located in a docker container, which was running over a WSL Linux connection. You can use any postgres connection you like. Just add the correct parameters in the ``.env`` file.

## License

This project is licensed under the MIT License. See `LICENSE` for more information.