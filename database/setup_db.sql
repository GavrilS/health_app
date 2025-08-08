SELECT 'CREATE DATABASE health_articles'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'health_articles')\gexec

USE DATABASE health_articles;

CREATE TABLE IF NOT EXISTS users (
    id,
    full_name,
    user_name,
    email,
    password,
    type
)

CREATE TABLE IF NOT EXISTS articles (
    id,
    title,
    description,
    data,
    image_gallery_id,
    video_gallery_id
)

CREATE TABLE IF NOT EXISTS image_gallery (
    id,
    image,
    sub_topic,
    article_id
)

CREATE TABLE IF NOT EXISTS video_gallery (
    id,
    video_link,
    sub_topic,
    article_id
)