-- use aggregation functions including COUNT, AVG, SUM.

-- count all rows
SELECT COUNT(*) FROM books;

-- count unique genres
SELECT COUNT(DISTINCT genre) FROM books;

-- get average amount
SELECT AVG(goodreads_rating) FROM books;

-- combine functions
SELECT SUM(goodreads_rating), AVG(goodreads_rating), COUNT(*) FROM books;