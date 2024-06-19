--This script uses the database to lists all genres of a show
SELECT tv_genres.name
FROM tv_shows
JOIN tv_genres ON tv_shows.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
