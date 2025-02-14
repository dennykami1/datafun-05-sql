# Use Python to execute the SQL queries and maybe chart, illustrate, and/or summarize your findings

import sqlite3
import pathlib
import pandas as pd

# Import local modules
from utils_logger import logger

# Define the database file path
db_file = pathlib.Path("project.sqlite3")

def query_aggregation():
    """Function to query the database and perform aggregation"""

    # Define the path to the SQL file
    sql_file = pathlib.Path("sql_queries", "query_aggregation.sql")

    # Connect to the SQLite database and execute the SQL script
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        
        # Read the SQL script file
        with open(sql_file, "r", encoding="utf-8") as file:
            sql_script = file.read()

        # Split the script into individual queries
        queries = sql_script.split(';')
        
        # Execute each query and print the results
        for query in queries:
            query = query.strip()
            if query:
                cursor.execute(query)
                result = cursor.fetchall()
                logger.info(f"Query: {query}")
                logger.info("Result:")
                for row in result:
                    logger.info(row)

    logger.info("Aggregation query executed successfully.")


def query_filter():
    """Function to query the database and perform filtering"""

    # Define the path to the SQL file
    sql_file = pathlib.Path("sql_queries", "query_filter.sql")

    # Connect to the SQLite database and execute the SQL script
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        
        # Read the SQL script file
        with open(sql_file, "r", encoding="utf-8") as file:
            sql_script = file.read()

        # Split the script into individual queries
        queries = sql_script.split(';')
        
        # Execute each query and print the results
        for query in queries:
            query = query.strip()
            if query:
                cursor.execute(query)
                result = cursor.fetchall()
                logger.info(f"Query: {query}")
                logger.info("Result:")
                for row in result:
                    logger.info(row)

    logger.info("Filtering query executed successfully.")

def query_group_by_sql():
    """Function to query the database and perform grouping"""

    # Define the path to the SQL file
    sql_file = pathlib.Path("sql_queries", "query_group_by.sql")

    # Connect to the SQLite database and execute the SQL script
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        
        # Read the SQL script file
        with open(sql_file, "r", encoding="utf-8") as file:
            sql_script = file.read()

        # Split the script into individual queries
        queries = sql_script.split(';')
        
        # Execute each query and print the results
        for query in queries:
            query = query.strip()
            if query:
                cursor.execute(query)
                result = cursor.fetchall()
                logger.info(f"Query: {query}")
                logger.info("Result:")
                for row in result:
                    logger.info(row)

    logger.info("Grouping query executed successfully.")


def query_sorting():
    """Function to sort the query results"""

    # Define the path to the SQL file
    sql_file = pathlib.Path("sql_queries", "query_sorting.sql")

    # Connect to the SQLite database and execute the SQL script
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        
        # Read the SQL script file
        with open(sql_file, "r", encoding="utf-8") as file:
            sql_script = file.read()

        # Split the script into individual queries
        queries = sql_script.split(';')
        
        # Execute each query and print the results
        for query in queries:
            query = query.strip()
            if query:
                cursor.execute(query)
                result = cursor.fetchall()
                logger.info(f"Query: {query}")
                logger.info("Result:")
                for row in result:
                    logger.info(row)

    logger.info("Sorting query executed successfully.")

def query_join():
    """Function to join tables"""

    # Define the path to the SQL file
    sql_file = pathlib.Path("sql_queries", "query_join.sql")

    # Connect to the SQLite database and execute the SQL script
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        
        # Read the SQL script file
        with open(sql_file, "r", encoding="utf-8") as file:
            sql_script = file.read()

        # Split the script into individual queries
        queries = sql_script.split(';')
        
        # Execute each query and print the results
        for query in queries:
            query = query.strip()
            if query:
                cursor.execute(query)
                result = cursor.fetchall()
                logger.info(f"Query: {query}")
                logger.info("Result:")
                for row in result:
                    logger.info(row)

    logger.info("Join query executed successfully.")


def main():
    query_aggregation()
    query_filter()
    query_group_by_sql()
    query_sorting()
    query_join()  

if __name__ == "__main__":
    main()