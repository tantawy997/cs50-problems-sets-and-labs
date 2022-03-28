/* select all names from songs table that have the word feat within the name of the song*/

select name from songs where name regexp "feat";