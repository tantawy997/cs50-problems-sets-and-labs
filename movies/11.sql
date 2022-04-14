-- write a SQL query to list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated.
-- Your query should output a table with a single column for the title of each movie.
-- You may assume that there is only one person in the database with the name Chadwick Boseman.


select movies.title from movies join stars, ratings, people on movies.id = ratings.movie_id and stars.person_id = people.id and movies.id = stars.movie_id where name = "Chadwick Boseman" order by rating desc limit 5;