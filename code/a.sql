# 用户评分表
select * from ods.ods_grouplens_ratings limit 3;
# Tag 评分
select * from ods.ods_grouplens_genome_scores limit 3;

# tag
select count(1) from ods.ods_grouplens_genome_tags limit 3;

select *
from ods.ods_grouplens_movies;


select count(1) from ods.ods_grouplens_movies;


select * from ods.ods_grouplens_movies m where m.title like '%Lebowski%'
select * from ods.ods_grouplens_tags t where t.movieId = '1732'