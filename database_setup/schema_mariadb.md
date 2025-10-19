# Tables
* users
    - id(ID) -> automatically generated
    - full_name(Text)**
    - user_name(Text) -> the in-app display name for the user; if empty will revert to the full_name
    - email(Text)**
    - password(Text)**
    - type(Text) -> 2 user types - admin and user(regular); will be populated automatically as a regular user, and the database manager will manually update the admins accounts

* articles
    - id(ID) -> automatically generated
    - title(Text)** -> the main title of the article
    - description(Text)** -> a brief description of the article theme
    - category(Text)** -> one of nutrition(default value), physical_activities and mental_activities

* segment
    - id(ID) -> automatically generated
    - heading(Text)** -> the heading of the segment
    - description(Text)** -> the information body of the article segment
    - order(int)** -> the order of appearance in the article layout
    - article_id(ID)** -> the ID of the article it is a part of

* image_gallery
    - id(ID) -> automatically generated
    - image(Blob) -> an image that is relevant for the associated article
    - article_id(ID) -> foreign-key to the articles table
    - segment_id(ID) -> the id of the segment under which it will be shown
    ** Either article_id or segment_id or both need to be populated

* video_gallery
    - id(ID) -> automatically generated
    - video_link(Text) -> a link to a video relevant for the associated article
    - article_id(ID) -> foreign-key to the articles table
    - segment_id(ID) -> the id of the segment under which it will be shown
    ** Either article_id or segment_id or both need to be populated

^^ Legend:
    ** -> required field