/* select all teh names from songs table where the id is their arist id from artist table */


select name from songs where artist_id  in  (select id  from artists where id = "54" ) ;