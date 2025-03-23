#
select m.year,t.tag,a.cleaned_title,a.avg_rating,a.comment_cnt,a.Id from dwd.tmp_movie_avg_rate_above_1000 a
    left join dwd.tags t on a.tagId = t.tagId
      left join dwd.movies m on a.cleaned_title = m.cleaned_title
   where a.comment_cnt > 1 and a.avg_rating< 2
order by avg_rating asc
;

select b.ID,
       count(1) as number_of_movies,avg(avg_rating) as rating_avg,sum(a.comment_cnt) as comment_count
from dwd.tmp_movie_avg_rate_above_1000 a

left join dwd.movies_genres b on a.movieId = b.movieId
group by b.ID
order by rating_avg desc
