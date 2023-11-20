-- Lists all genres from the database hbtn_0d_tvshows along with the number of
-- shows linked to each.
-- Does not display genres without linked shows.
-- Records are ordered by descending number of shows linked.
SELECT name as "name", count(*) as "number_of_shows"
FROM tv_genres tg
LEFT JOIN tv_show_genres tsg
ON tg.id = tsg.genre_id
group by tg.name
ORDER BY `number_of_shows` DESC;