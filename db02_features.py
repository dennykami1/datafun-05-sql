# Create a Python script that demonstrates the ability to run sql scripts to interact with fields, update records, delete records, and maybe add additional columns.

import sqlite3
import pathlib
import pandas as pd

# Import local modules
from utils_logger import logger

# Define the database file path
db_file = pathlib.Path("project.sqlite3")

def delete_records():
    """Function to delete records from the database"""

    # Define the path to the SQL file
    sql_file = pathlib.Path("sql_features", "delete_records.sql")

    # Connect to the SQLite database and execute the SQL script
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        
        # Read the SQL script file
        with open(sql_file, "r", encoding="utf-8") as file:
            sql_script = file.read()
        
        # Execute the SQL script
        cursor.executescript(sql_script)

    logger.info("Records deleted successfully.")

def update_records():
    """Function to update records in the database"""

    # Define the path to the SQL file
    sql_file = pathlib.Path("sql_features", "update_records.sql")

    # Connect to the SQLite database and execute the SQL script
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        
        # Read the SQL script file
        with open(sql_file, "r", encoding="utf-8") as file:
            sql_script = file.read()
        
        # Execute the SQL script
        cursor.executescript(sql_script)

    logger.info("Records updated successfully.")

def main():
    delete_records()
    update_records()

if __name__ == "__main__":
    main()