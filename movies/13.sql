--  write a SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starred.
-- Your query should output a table with a single column for the name of each person.
-- There may be multiple people named Kevin Bacon in the database. Be sure to only select the Kevin Bacon born in 1958.
-- Kevin Bacon himself should not be included in the resulting list.



 
select distinct people.name from people join stars, movies on people.id = stars.person_id and movies.id = stars.movie_id where stars.movie_id in (select stars.movie_id from people join stars, movies on people.id = stars.person_id and movies.id = stars.movie_id where people.name = "Kevin Bacon") and people.name <> "Kevin Bacon";