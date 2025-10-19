DROP DATABASE IF EXISTS health_articles;

CREATE DATABASE health_articles;

USE health_articles;

SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id UUID DEFAULT UUID_v4(),
    full_name VARCHAR(100),
    user_name VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE,
    password VARCHAR(50) NOT NULL,
    type VARCHAR(30) DEFAULT 'regular',
    PRIMARY KEY (id)
);

INSERT INTO users (user_name, password, type)
VALUES ('admin', 'admin', 'admin');

DROP TABLE IF EXISTS articles;

CREATE TABLE articles (
    id UUID DEFAULT UUID_v4(),
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    category VARCHAR(20) DEFAULT 'nutrition',
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS segments;

CREATE TABLE segments (
    id UUID DEFAULT UUID_v4(),
    heading VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    segment_order TINYINT UNSIGNED,
    article_id UUID,
    PRIMARY KEY (id),
    CONSTRAINT fk_segment_articles
        FOREIGN KEY(article_id)
        REFERENCES articles(id)
        ON DELETE CASCADE
);

DROP TABLE IF EXISTS image_gallery;

CREATE TABLE image_gallery (
    id UUID DEFAULT UUID_v4(),
    image TEXT NOT NULL,
    segment_id UUID,
    article_id UUID,
    PRIMARY KEY (id),
    CONSTRAINT fk_image_articles
        FOREIGN KEY(article_id)
        REFERENCES articles(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_image_segments
        FOREIGN KEY(segment_id)
        REFERENCES segments(id)
        ON DELETE CASCADE
);

DROP TABLE IF EXISTS video_gallery;

CREATE TABLE video_gallery (
    id UUID DEFAULT UUID_v4(),
    video_link TEXT NOT NULL,
    segment_id UUID,
    article_id UUID,
    PRIMARY KEY (id),
    CONSTRAINT fk_video_articles
        FOREIGN KEY(article_id)
        REFERENCES articles(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_video_segments
        FOREIGN KEY(segment_id)
        REFERENCES segments(id)
        ON DELETE CASCADE
);

SET FOREIGN_KEY_CHECKS=1;