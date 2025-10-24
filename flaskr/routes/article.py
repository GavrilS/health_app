'''
This file holds the article related routes functionalities:
- load articles by category
- create a new article
- load an article
- update an article
- delete an article
'''

from flask import (
    Blueprint, render_template, url_for
)

article = Blueprint('article', __name__, template_folder='templates/articles')


@article.route('/article/<category>', methods=('GET', 'POST'))
def show_articles_by_category(category):
    '''
    Load the articles page with all articles from the specified category:
    - pull all articles by category from db
    - make a list of titles to display as links to separate articles
    - populate the list on the page

    <category>:
        - one of nutrition, physical_activity, mental_activity
    '''