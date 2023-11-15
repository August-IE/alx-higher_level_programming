-- A scripts that uses the hbtn_0d_tvshows database to list all genres
-- not linked to the show Dexter.
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
SELECT DISTINCT name
 FROM tv_genres
      WHERE NOT EXISTS (
   	    SELECT 1
	    FROM tv_show_genres
    	    INNER JOIN tv_shows 
	    ON tv_show_genres.show_id = tv_shows.id
      WHERE tv_shows.title = 'Dexter'
	    AND tv_genres.id = tv_show_genres.genre_id
)
ORDER BY name;
