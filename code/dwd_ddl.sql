create table dwd_movie
(
    movie_name,
    year,
    length,
)

;

insert into dwd_movie
from
    select
        moive
    from ods_imdb_user
    union all
    select
        moive
    from ods_cum_movie;


