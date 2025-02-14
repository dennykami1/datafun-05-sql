# Create a Python script that demonstrates the ability to create a database, define a schema, and insert records. Make it easy to re-run by dropping the tables first.

import sqlite3
import pandas as pd
import pathlib

# Import local modules
from utils_logger import logger

# Define the database file in the current root project directory
db_file = pathlib.Path("project.sqlite3")

def create_database():
    """Function to create a database file"""
    
    # Drop the Tables if they exist
    with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_create", "01_drop_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logger.info("Tables dropped successfully.")
    
    # Create the Tables
    with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql_create", "02_create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logger.info("Tables created successfully.")

def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        author_data_path = pathlib.Path("data", "authors.csv")
        book_data_path = pathlib.Path("data", "books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            logger.info("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        logger.error("Error inserting data:", e)

def insert_records():
    """Function to insert records into the database"""

    # Define the path to the SQL file
    sql_file = pathlib.Path("sql_create", "03_Insert_Records.sql")

    # Connect to the SQLite database and execute the SQL script
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        
        # Read the SQL script file
        with open(sql_file, "r", encoding="utf-8") as file:
            sql_script = file.read()
        
        # Execute the SQL script
        cursor.executescript(sql_script)

    logger.info("Records inserted successfully.")

logger.info("Database created successfully.")

def main():
    create_database()
    insert_data_from_csv()
    insert_records()

if __name__ == "__main__":
    main()