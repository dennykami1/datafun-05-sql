-- create your database schema using sql

-- create the authors table
CREATE TABLE authors (
    author_id TEXT PRIMARY KEY,
    first TEXT NOT NULL,
    last TEXT NOT NULL
);

-- create the books table
CREATE TABLE books (
    book_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    goodreads_rating REAL NOT NULL,
    author_id TEXT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);