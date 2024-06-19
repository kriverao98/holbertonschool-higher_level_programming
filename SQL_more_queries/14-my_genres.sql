--This script uses the database to lists all genres of a show
SELECT name FROM tv_genres
JOIN tv_shows ON id=tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY name;
