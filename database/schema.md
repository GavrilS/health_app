# Tables
* users
    - id(ID) -> automatically generated
    - full_name(Text)**
    - user_name(Text) -> the in-app display name for the user; if empty will revert to the full_name
    - email(Text)**
    - password(Text)**
    - type(Text) -> 2 user types - admin and regular; will be populated automatically as a regular, and the database manager will manually update the admins accounts

* articles
    - id(ID) -> automatically generated
    - title(Text)** -> the main title of the article
    - description(Text)** -> a brief description of the article theme
    - data(JSON) -> in-depth information about the topic of the article; json format field, where the keys are sub-topics and their values are the information related to the sub-topic
    - image_gallery_id(ID) -> foreign-key to the image_gallery table, where we have photos, relevant for this page; Many-To-Many relation
    - video_gallery_id(ID) -> foreign-key to the video_gallery table, where we have relevant video links for this article; Many-To-Many relation

* image_gallery
    - id(ID) -> automatically generated
    - image(Blob) -> an image that is relevant for the associated article
    - sub_topic(Text) -> which section of the article this image relates to; if not provided it will go to the default gallery section of the article
    - article_id(ID) -> foreign-key to the articles table; Many-To-Many relation

* video_gallery
    - id(ID) -> automatically generated
    - video_link(Text) -> a link to a video relevant for the associated article
    - sub_topic(Text) -> which section of the article this video relates to; if not provided it will go to the default gallery section of the article
    - article_id(ID) -> foreign-key to the articles table; Many-To-Many relation

^^ Legend:
    ** -> required field