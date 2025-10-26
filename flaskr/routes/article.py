'''
This file holds the article related routes functionalities:
- load articles by category
- create a new article
- load an article
- update an article
- delete an article
'''

from flask import (
    Blueprint, render_template, url_for, request
)

article = Blueprint('article', __name__, template_folder='templates/articles')

from flaskr.db.models.article import Article
from flaskr.db.models.segment import Segment
from flaskr.db.models.user import User
from flaskr.db.operation_manager import OperationManager
from flaskr.db.query_manager import QueryManager

operation_manager = OperationManager()
query_manager = QueryManager()


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
    articles = []
    operation_manager.set_db_connection()
    data = {
        'articles': articles,
        'category': category
    }

    if request.method == 'POST':
        article = Article(
            title=request.form.get('title', None),
            description=request.form.get('description', None),
            category=request.form.get('category', category)
        )

        query = query_manager.make_insert_query(article, 'articles')
        print('Query: ', query)
        res = operation_manager.execute_query(query)
        print('DB response: ', res)

    query = query_manager.make_get_query('articles', category)
    res = operation_manager.execute_query(query)
    operation_manager.close_db_connection()
    for item in res:
        # TODO add error handling when building articles
        article = Article(id=item[0], title=item[1], description=item[2], category=item[3])
        articles.append(article)
    
    # print('Articles: ', articles)
    return render_template('articles/category.html', data=data)


@article.route('/article/<category>/<article_id>', methods=('GET', 'POST'))
def open_article(category, article_id):
    '''
    Load the respective article page:
    - display the article content
    - keep a reference to the list of articles of the same category
    '''
    articles = []
    data = {
        'articles': articles
    }
    operation_manager.set_db_connection()

    print(1)

    if request.method == 'POST':
        print(2)
        if request.form.get('_method', '') == 'PUT':
            print('Updating an article')
            article = Article(
                id=article_id,
                title=request.form['title'],
                description=request.form['description'],
                category=category
            )
            print(3)
            query = query_manager.make_update_query_by_id(article, 'articles')
            print('Query: ', query)
            res = operation_manager.execute_query(query)
            print('DB response: ', res)
            print(4)
        elif request.form.get('_method') == 'DELETE':
            print('Deleting an article')
            article = Article(
                id=article_id,
                title=request.form['title'],
                description=request.form['description'],
                category=category
            )
            print(5)
            query = query_manager.make_remove_query_id(article, 'articles')
            print('Query: ', query)
            res = operation_manager.execute_query(query)
            print('DB response: ', res)
            print(6)
            return url_for('article.show_articles_by_category', category=category)
    
    print('Getting an article')
    query = query_manager.make_get_query('articles', category)
    res = operation_manager.execute_query(query)
    print(7)
    operation_manager.close_db_connection()
    print(8)
    for item in res:
        # TODO add error handling when building articles
        article = Article(id=item[0], title=item[1], description=item[2], category=item[3])
        if article.id == article_id:
            data['current_article'] = article
        else:
            articles.append(article)
    print(9)
    return render_template('articles/article.html', data=data)