/* select the avg energy from songs where the artist id is 23 */

select avg(energy) from songs where artist_id in (select id from artists where id = "23");