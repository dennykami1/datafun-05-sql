-- update 1 or more records in a table.

--Update Year Born for Author Alice Hoffman
UPDATE authors
SET year_born = 1952
WHERE last_name = 'Hoffman';

--Update Year Born for Author Sarah J Maas
UPDATE authors
SET year_born = 1986
WHERE last_name = 'Maas';

--Update Year Born for Author Rebecca Yarros
UPDATE authors
SET year_born = 1981
WHERE last_name = 'Yarros';

--Update Year Born for Author Emily Henry
UPDATE authors
SET year_born = 1986
WHERE last_name = 'Henry';

-- Update the genre for Happy Place
UPDATE books
SET genre = 'Womens Fiction'
WHERE title = 'Happy Place';