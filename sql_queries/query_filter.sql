-- use WHERE to filter data based on conditions.

-- get all books with a rating above 4.5
SELECT * FROM books WHERE goodreads_rating > 4.5;

-- get all books with a rating above 4.5 and published after 2000
SELECT * FROM books WHERE goodreads_rating > 4.5 AND year_published > 2000;

-- select fantasy books with a rating greater than 4.5
SELECT * FROM books WHERE genre = 'Fantasy' OR goodreads_rating > 4.5;