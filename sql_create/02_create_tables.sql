-- create your database schema using sql

-- create the authors table
CREATE TABLE authors (
    author_id TEXT PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    year_born INTEGER
);

-- create the books table
CREATE TABLE books (
    book_id TEXT PRIMARY KEY,
    Title TEXT,
    year_published INTEGER NOT NULL,
    genre TEXT NOT NULL,
    goodreads_rating REAL NOT NULL,
    author_id TEXT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);