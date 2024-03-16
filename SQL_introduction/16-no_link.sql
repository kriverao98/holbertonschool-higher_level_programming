-- lists all records of second table where name is not NULL ordered by score
SELECT score, name FROM second_table WHERE name!='' OR name IS NOT NULL ORDER BY score DESC;