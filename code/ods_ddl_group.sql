

DROP TABLE IF EXISTS ods.ods_grouplens_genome_scores;
CREATE TABLE ods.ods_grouplens_genome_scores (
    movieId VARCHAR(512),
    tagId VARCHAR(512),
    relevance VARCHAR(512),
    PRIMARY KEY (movieId, tagId)
);

DROP TABLE IF EXISTS ods.ods_grouplens_genome_tags;
CREATE TABLE ods.ods_grouplens_genome_tags (
    tagId VARCHAR(512) PRIMARY KEY,
    tag VARCHAR(512)
);

DROP TABLE IF EXISTS ods.ods_grouplens_links;
CREATE TABLE ods.ods_grouplens_links (
    movieId VARCHAR(512),
    imdbId VARCHAR(512),
    tmdbId VARCHAR(512),
    PRIMARY KEY (movieId)
);

DROP TABLE IF EXISTS ods.ods_grouplens_movies;
CREATE TABLE ods.ods_grouplens_movies (
    movieId VARCHAR(512) PRIMARY KEY,
    title VARCHAR(512),
    genres VARCHAR(512)
);

DROP TABLE IF EXISTS ods.ods_grouplens_ratings;
CREATE TABLE ods.ods_grouplens_ratings (
    userId VARCHAR(512),
    movieId VARCHAR(512),
    rating VARCHAR(512),
    timestamp VARCHAR(512),
    PRIMARY KEY (userId, movieId)
);

DROP TABLE IF EXISTS ods.ods_grouplens_tags;
CREATE TABLE ods.ods_grouplens_tags (
    userId VARCHAR(512),
    movieId VARCHAR(512),
    tag VARCHAR(512),
    timestamp VARCHAR(512),
    PRIMARY KEY (userId, movieId, tag)
);
