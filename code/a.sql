select * from ods.ods_grouplens_ratings limit 3;
# Tag 评分
select * from ods.ods_grouplens_genome_scores limit 3;

# tag
select count(1) from ods.ods_grouplens_genome_tags limit 3;

select *
from ods.ods_grouplens_movies;


select count(1) from ods.ods_grouplens_movies;

select *
from ods.ods_grouplens_genome_tags;
;
select
    m.movieId,
    m.title,
    count(1)
#     m.genres

from ods.ods_grouplens_movies m
left join ods.ods_grouplens_genome_scores s on m.movieId = s.movieId
group by m.movieId, m.title
;

select * from ods.ods_grouplens_genome_tags;

# fenxi
select count(distinct r.movieId)
    from ods.ods_grouplens_genome_scores r
where r.relevance > 0.5
;

select * from
ods.ods_grouplens_genome_scores r;


create table dwd.dwd_grouplens_genome_scores as
select
    r.movieId,r.tagId,o.max_relevance
from ods.ods_grouplens_genome_scores r
inner join
(
    select movieId,max(r.relevance) as max_relevance
from  ods.ods_grouplens_genome_scores r
group by r.movieId
) o on r.movieId = o.movieId and r.relevance = o.max_relevance

;

select * from ods.ods_grouplens_movies m where m.title like '%Lebowski%';
select * from ods.ods_grouplens_tags t where t.movieId = '1732';



select count(distinct movieId) from ods.ods_grouplens_genome_scores;

select count(1) from dwd.dwd_grouplens_genome_scores;

create table dwd.movies as
select
    m.movieId,
    m.title as uncleaned_title,
    case when m.title REGEXP '\\([0-9]{4}\\)$'
        then trim(replace(m.title,RIGHT(m.title, 6),''))
    else m.title
        end as cleaned_title,
    case when m.title REGEXP '\\([0-9]{4}\\)$'
        then replace(replace(RIGHT(m.title, 6),'(',''),')','')
        else '-1'
        end as year
from ods.ods_grouplens_movies m


;

select count(1) from ods.ods_grouplens_movies m
where m.title like '%)'
;
select count(1) from ods.ods_grouplens_movies ;

SELECT 'sdfsdf(1991)' not REGEXP '\\([0-9]{4}\\)$';   -- 返回 0，因为 'abc' 不匹配 'd' 模式
create table dwd.movies_genres
SELECT
    a.movieId,
    substring_index(substring_index(a.genres,'_',b.help_topic_id + 1    ),    '|' ,- 1    ) AS ID
from
(select
    m.movieId,
    genres
    from ods.ods_grouplens_movies m
    ) a
JOIN mysql.help_topic b ON b.help_topic_id <
(length(a.genres) - length( replace(a.genres, '|', '')  ) + 1)
;

SELECT
    substring_index(substring_index(a.chain,'_',b.help_topic_id + 1    ),    '_' ,- 1    ) AS ID
FROM
    (select '1_11_1223_1242' as chain) a
JOIN mysql.help_topic b ON b.help_topic_id <
(length(a.chain) - length( replace(a.chain, '_', '')  ) + 1)

;

select count(distinct movieId) from dwd.movies_genres;

select count(distinct movieId) from ods.ods_grouplens_movies