-- insert at least 10 additional records into each table.

-- Insert authors data
INSERT INTO authors (author_id, first_name, last_name, year_born)
VALUES
    ('a1b2c3d4-5678-90ab-cdef-1234567890ab','Alice','Hoffman', NULL),
    ('b2c3d4e5-6789-01bc-def2-3456789012cd','Sarah J','Maas', NULL),
    ('c3d4e5f6-7890-12cd-ef34-5678901234de','Rebecca','Yarros', NULL),
    ('e5f6g7h8-9012-34ef-5678-9012345678gh','Emily','Henry', NULL);

-- Insert books data
INSERT INTO books (book_id, title, year_published, genre, goodreads_rating, author_id)
VALUES
    ('1a2b3c4d-5678-90ab-cdef-1234567890ab', 'Magic Lessons', 2020, 'Historical Fiction', 4.22, 'a1b2c3d4-5678-90ab-cdef-1234567890ab'),
    ('2b3c4d5e-6789-01bc-def2-3456789012cd', 'Throne of Glass', 2012, 'Fantasy', 4.18, 'b2c3d4e5-6789-01bc-def2-3456789012cd'),
    ('3c4d5e6f-7890-12cd-ef34-5678901234de', 'Fourth Wing', 2023, 'Fantasy', 4.58, 'c3d4e5f6-7890-12cd-ef34-5678901234de'),
    ('5e6f7g8h-9012-34ef-5678-9012345678gh', 'Happy Place', 2023, 'Romance', 3.97,'e5f6g7h8-9012-34ef-5678-9012345678gh');