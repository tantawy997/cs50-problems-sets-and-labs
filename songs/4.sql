/* select all the names of the songs from the the songs table where energy and velence and danceability are greter than 0.75*/

SELECT name
FROM songs
where valence > 0.75 and energy > 0.75 and danceability > 0.75;