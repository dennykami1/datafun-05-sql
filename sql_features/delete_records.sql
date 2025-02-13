-- delete 1 or more records from a table.

-- Delete books with the following titles
DELETE FROM books WHERE Title IN ('The Lord of the Rings', 'The Hobbit');

-- Delete where Tolkein is the author
DELETE FROM authors WHERE last_name = 'Tolkien';

-- Delete books with a rating less than 3.85
DELETE FROM books WHERE goodreads_rating < 3.85;