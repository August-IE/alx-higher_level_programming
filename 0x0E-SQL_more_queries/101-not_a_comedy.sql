-- A script that lists all shows without the genre Comedy
-- in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title.
-- Results must be sorted in ascending order by the show title.
SELECT DISTINCT title
  FROM tv_shows
       WHERE NOT EXISTS (
             SELECT 1
             FROM tv_show_genres
                 INNER JOIN tv_genres 
		 ON tv_genres.id = tv_show_genres.genre_id
       WHERE tv_show_genres.show_id = tv_shows.id
       AND tv_genres.name = 'Comedy'
)
ORDER BY title;
