import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os


class PostgresConnector:
    """Class for connecting to PostgreSQL database, creating a table and inserting data from books.csv file."""
    def __init__(self, host, database, user, password, port):
        """Initializes the PostgresConnector"""
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        """Connects to the PostgreSQL database using the provided credentials."""
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            self.cursor = self.connection.cursor()
        except psycopg2.Error as e:
            print(f"Unable to connect to the database: {e}")

    def create_table(self):
        """"Creates a table in the PostgreSQL database to store the CSV data."""
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS books (name TEXT, category TEXT, stars TEXT, price TEXT, is_stock TEXT);")
        except psycopg2.Error as e:
            print(f"Error creating table: {e}")

    def insert_data(self, csv_file):
        """Inserts data from a CSV file into the books table in the PostgreSQL database."""
        try:
            df_books = pd.read_csv(csv_file)
            for index, row in df_books.iterrows():
                self.cursor.execute(
                    "SELECT COUNT(*) FROM books WHERE name = %s AND category = %s AND stars = %s AND price = %s AND is_stock = %s",
                    (row['Book Name'], row['Book Category'], row['Book Star Rating'], row['Book Price'], row['Book in Stock'])
                )
                row_count = self.cursor.fetchone()[0]
                if row_count == 0:
                    self.cursor.execute(
                        "INSERT INTO books (name, category, stars, price, is_stock) VALUES (%s, %s, %s, %s, %s);",
                        (row['Book Name'], row['Book Category'], row['Book Star Rating'], row['Book Price'], row['Book in Stock'])
                    )
                    print('Data entered into the table!')
                else:
                    print('The data already exists in the table.')
            self.connection.commit()
        except psycopg2.Error as e:
            print(f"Error inserting data: {e}")


    def disconnect(self):
        """Disconnects from the PostgreSQL database."""
        try:
            self.cursor.close()
            self.connection.close()
        except psycopg2.Error as e:
            print(f"Error disconnecting from the database: {e}")

if __name__ == '__main__':
    load_dotenv()  
    connector = PostgresConnector(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        port=os.getenv('DB_PORT')
    )

    connector.connect()
    connector.create_table()
    connector.insert_data('books.csv')
    connector.disconnect()