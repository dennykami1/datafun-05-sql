-- use GROUP BY clause (and optionally with aggregation)

-- Get the average goodreads_rating by genre
SELECT genre, AVG(goodreads_rating)
FROM books
GROUP BY genre;

-- Get the count of books by genre
SELECT genre, COUNT(*) as count
FROM books
GROUP BY genre;