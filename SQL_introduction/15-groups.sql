-- This script lists all nums of records with same score
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
