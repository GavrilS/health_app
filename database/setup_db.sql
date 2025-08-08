SELECT 'CREATE DATABASE health_articles'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'health_articles')\gexec

USE DATABASE health_articles;

CREATE TABLE IF NOT EXISTS users (
    id UUID DEFAULT get_random_uuid(),
    full_name VARCHAR(100),
    user_name VARCHAR(50) NOT NULL,
    email VARCHAR(50),
    password VARCHAR(50) NOT NULL,
    type VARCHAR(30) DEFAULT 'regular',
    PRIMARY KEY (id)
)

INSERT INTO users (user_name, password, type)
VALUES ('admin', 'admin', 'admin');

CREATE TABLE IF NOT EXISTS articles (
    id UUID DEFAULT get_random_uuid(),
    title VARCHAR(100) NOT NULL,
    description TEXT DEFAULT '',
    sections JSON DEFAULT '{}',
    PRIMARY KEY (id)
)

CREATE TABLE IF NOT EXISTS image_gallery (
    id UUID DEFAULT get_random_uuid(),
    image,
    sub_topic VARCHAR(100),
    article_id UUID,
    PRIMARY KEY (id),
    CONSTRAINT fk_articles
        FOREIGN KEY(article_id)
        REFERENCES articles(id)
        ON DELETE CASCADE
)

CREATE TABLE IF NOT EXISTS video_gallery (
    id UUID DEFAULT get_random_uuid(),
    video_link TEXT NOT NULL,
    sub_topic VARCHAR(100),
    article_id,
    PRIMARY KEY (id),
    CONSTRAINT fk_articles
        FOREIGN KEY(article_id)
        REFERENCES articles(id)
        ON DELETE CASCADE
)