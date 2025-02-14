-- use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.

-- left join authors and books on author_id
SELECT authors.last_name, books.title, books.year_published, books.goodreads_rating, books.genre
FROM authors
INNER JOIN books ON authors.author_id = books.author_id;
