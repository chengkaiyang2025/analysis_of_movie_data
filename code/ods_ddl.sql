DROP TABLE IF EXISTS ods.ods_imdb_name_basics;
CREATE TABLE ods.ods_imdb_name_basics (
    nconst VARCHAR(512) PRIMARY KEY,
    primaryName VARCHAR(512),
    birthYear VARCHAR(512),
    deathYear VARCHAR(512),
    primaryProfession VARCHAR(512),
    knownForTitles VARCHAR(512)
);

DROP TABLE IF EXISTS ods.ods_imdb_akas;
CREATE TABLE ods.ods_imdb_akas (
    titleId VARCHAR(512),
    ordering VARCHAR(512),
    title VARCHAR(512),
    region VARCHAR(512) NULL,
    language VARCHAR(512) NULL,
    types VARCHAR(512) NULL,
    attributes VARCHAR(512) NULL,
    isOriginalTitle VARCHAR(512),
    PRIMARY KEY (titleId, ordering)
);

DROP TABLE IF EXISTS ods.ods_imdb_basics;
CREATE TABLE ods.ods_imdb_basics (
    tconst VARCHAR(512) PRIMARY KEY,
    titleType VARCHAR(512),
    primaryTitle VARCHAR(512),
    originalTitle VARCHAR(512),
    isAdult VARCHAR(512),
    startYear VARCHAR(512),
    endYear VARCHAR(512),
    runtimeMinutes VARCHAR(512),
    genres VARCHAR(512)
);

DROP TABLE IF EXISTS ods.ods_imdb_crew;
CREATE TABLE ods.ods_imdb_crew (
    tconst VARCHAR(512) PRIMARY KEY,
    directors VARCHAR(512),
    writers VARCHAR(512)
);

DROP TABLE IF EXISTS ods.ods_imdb_episode;
CREATE TABLE ods.ods_imdb_episode (
    tconst VARCHAR(512) PRIMARY KEY,
    parentTconst VARCHAR(512),
    seasonNumber VARCHAR(512),
    episodeNumber VARCHAR(512)
);

DROP TABLE IF EXISTS ods.ods_imdb_principals;
CREATE TABLE ods.ods_imdb_principals (
    tconst VARCHAR(512),
    ordering VARCHAR(512),
    nconst VARCHAR(512),
    category VARCHAR(512),
    job VARCHAR(512),
    characters VARCHAR(512),
    PRIMARY KEY (tconst, ordering)
);

DROP TABLE IF EXISTS ods.ods_imdb_rating;
CREATE TABLE ods.ods_imdb_rating (
    tconst VARCHAR(20) NULL,
    averageRating VARCHAR(512) NULL,
    numVotes VARCHAR(512) NULL
);
