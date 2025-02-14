# **datafun-05-sql**

# **Description:**
Project 5 integrates Python and SQL, focusing on database interactions using SQLite. The project involves creating and managing a database, building a schema, and performing various SQL operations, including queries with joins, filters, and aggregations.

# **How to run the project yourself:**

**Cloned and Opened my Github project**
```
cd \Projects
git clone https://github.com/dennykami1/datafun-05-sql
cd datafun-04-eda-
```


**Created a .gitignore file, and pasted in contents from example**
```
# Python virtual environment
.venv/

# Visual Studio Code settings and workspace
.vscode/

# Compiled Python files
__pycache__/

# macOS system files
.DS_Store
```

**Commited Changes to Github**
```
git add .
git commit -m "Add .gitignore"
git push -u origin main
```

**Created Virtual Environment and Activated**
```
py -m venv .venv
.venv\Scripts\activate
```

**Upgrade pip & install requirements.txt**
```
py -m pip install --upgrade pip setuptools wheel
py -m pip install -r requirements.txt
```

# **Summary of Project**

## **db01_setup.py**

### This Python script automates the creation of an SQLite database, defines its schema, and inserts records from CSV files and SQL scripts.

### **Features:**
#### Drops existing tables to ensure a fresh start.
#### Creates tables using SQL schema files.
#### Inserts data from CSV files and an SQL script.
#### Uses Pandas for CSV data handling and SQLite for database management.
#### Includes logging for tracking execution.

### **Placed SQL schema files in the sql_create folder:**
#### 01_drop_tables.sql - drop tables to restart
#### 02_create_tables.sql - create authors and books database schema using sql
#### 03_insert_records.sql - insert records

![alt text](table_after_db01_setup.png)

---

## **db02_setup.py**

### This Python script runs SQL scripts to interact with database fields, update records, delete records, and potentially modify the schema.

### **Features:**
#### Deletes records using a predefined SQL script.
#### Updates records based on specified conditions.
#### Uses SQLite for database management and logging for execution tracking.

#### **Store SQL scripts in the sql_features folder:**
#### delete_records.sql - Handles record deletion
#### update_records.sql - Updates existing records

![alt text](table_after_db02.png)

---

## **db03_queries.py**

### This Python script executes SQL queries to analyze and manipulate data stored in an SQLite database. It runs various SQL operations and logs the results for further insights.

### **Features:**
#### Aggregation Queries: Summarizes data using SQL aggregate functions.
#### Filtering Queries: Extracts specific data based on conditions.
#### Grouping Queries: Groups data for better analysis.
#### Sorting Queries: Orders query results for improved readability.
#### Join Queries: Combines data from multiple tables.

### **Store SQL scripts in the sql_queries folder:**
#### query_aggregation.sql - Aggregates data
#### query_filter.sql - Filters data
#### query_group_by.sql - Groups results
#### query_sorting.sql - Sorts query output
#### query_join.sql - Joins tables

![alt text](log_after_db03.png)
