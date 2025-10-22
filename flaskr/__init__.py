import os
from flask import (
    Flask, render_template, url_for, request
)
from flaskr.db.models.article import Article
from flaskr.db.models.segment import Segment
from flaskr.db.models.user import User
from flaskr.db.operation_manager import OperationManager
from flaskr.db.query_manager import QueryManager


def create_app():
    app = Flask(__name__)

    operation_manager = OperationManager()
    query_manager = QueryManager()

    @app.route('/')
    def index():
        '''
        Load the home page:
        - no data needs to be passed
        '''
        return render_template('index.html')
    
    @app.route('/nutrition', methods=('GET', 'POST'))
    def show_nutrition_category():
        '''
        Load the nutrition category page:
        - pull all nutrition articles from db
        - make a list of titles to display as links to separate articles
        - populate the list on the page
        '''
        nutrition_articles = []
        operation_manager.set_db_connection()

        if request.method == 'POST':
            article = Article(
                title=request.form.get('title', None),
                description=request.form.get('description', None),
                category=request.form.get('category')
            )

            query = query_manager.make_insert_query(article, 'articles')
            print('Query: ', query)
            res = operation_manager.execute_query(query)
            print('DB response: ', res)

        query = query_manager.make_get_query('articles', 'nutrition')
        res = operation_manager.execute_query(query)
        operation_manager.close_db_connection()
        for item in res:
            # TODO add error handling when building articles
            article = Article(id=item[0], title=item[1], description=item[2], category=item[3])
            nutrition_articles.append(article)
        
        # print('Nutrition articles: ', nutrition_articles)
        return render_template('nutrition.html', articles=nutrition_articles)
    
    @app.route('/nutrition/<article_id>', methods=('GET', 'PUT', 'DELETE'))
    def show_nutrition_article(article_id):
        '''
        Load the respective nutrition article page:
        - display the nutrition article
        - keep a reference to the list of nutrition articles
        '''
        articles = []
        data = {
            'articles': articles
        }
        operation_manager.set_db_connection()

        if request.method == 'PUT':
            article = Article(
                id=request.form['id'],
                title=request.form['title'],
                description=request.form['description'],
                category=request.form['category']
            )

            query = query_manager.make_update_query_by_id(article, 'articles')
            print('Query: ', query)
            res = operation_manager.execute_query(query)
            print('DB response: ', res)

        elif request.method == 'DELETE':
            article = Article(
                id=request.form['id'],
                title=request.form['title'],
                description=request.form['description'],
                category=request.form['category']
            )

            query = query_manager.make_remove_query_id(article, 'articles')
            print('Query: ', query)
            res = operation_manager.execute_query(query)
            print('DB response: ', res)

            return url_for('/nutrition')
        
        query = query_manager.make_get_query('articles', 'nutrition')
        res = operation_manager.execute_query(query)
        operation_manager.close_db_connection()
        for item in res:
            # TODO add error handling when building articles
            article = Article(id=item[0], title=item[1], description=item[2], category=item[3])
            if article.id == article_id:
                data['current_article'] = article
            else:
                articles.append(article)

        return render_template('nutrition_article.html', data=data)
    
    @app.route('/physical_activities', methods=('GET', 'POST'))
    def show_physical_category():
        '''
        Load the physical activities category page:
        - pull all physical activity articles from db
        - make a list of titles to display as links to separate articles
        - populate the list on the page
        '''
        physical_activity_articles = []
        operation_manager.set_db_connection()

        if request.method == 'POST':
            article = Article(
                title=request.form.get('title', None),
                description=request.form.get('description', None),
                category=request.form.get('category', 'physical_activity')
            )

            query = query_manager.make_insert_query(article, 'articles')
            print('Query: ', query)
            res = operation_manager.execute_query(query)
            print('DB response: ', res)
        
        query = query_manager.make_get_query('articles', 'physical_activity')
        res = operation_manager.execute_query(query)
        operation_manager.close_db_connection()
        for item in res:
            # TODO add error handling when building articles
            article = Article(id=item[0], title=item[1], description=item[2], category=item[3])
            physical_activity_articles.append(article)
        
        # print('Physical activity articles: ', physical_activity_articles)
        return render_template('physical_activities.html', articles=physical_activity_articles)
    
    @app.route('/physical_activities/<article_id>')
    def show_physical_article(article_id):
        '''
        Load the respective physical activities article page:
        - load the article
        - make a list of available physical activities articles
        '''
        articles = []
        data = {
            'articles': articles
        }
        operation_manager.set_db_connection()

        if request.method == 'PUT':
            article = Article(
                id=request.form['id'],
                title=request.form['title'],
                description=request.form['description'],
                category=request.form['category']
            )

            query = query_manager.make_update_query_by_id(article, 'articles')
            print('Query: ', query)
            res = operation_manager.execute_query(query)
            print('DB response: ', res)

        elif request.method == 'DELETE':
            article = Article(
                id=request.form['id'],
                title=request.form['title'],
                description=request.form['description'],
                category=request.form['category']
            )

            query = query_manager.make_remove_query_id(article, 'articles')
            print('Query: ', query)
            res = operation_manager.execute_query(query)
            print('DB response: ', res)

            return url_for('/physical_activities')
        
        query = query_manager.make_get_query('articles', 'physical_activity')
        res = operation_manager.execute_query(query)
        operation_manager.close_db_connection()
        for item in res:
            # TODO add error handling when building articles
            article = Article(id=item[0], title=item[1], description=item[2], category=item[3])
            if article.id == article_id:
                data['current_article'] = article
            else:
                articles.append(article)

        return render_template('physical_activities_article.html', data=data)
    
    @app.route('/mental_activities')
    def show_mind_category():
        '''
        Load the mental activities category page:
        - pull all mental activity articles from db
        - make a listphysical_activity_articles of titles to display as links to separate articles
        - populate the list on the page
        '''
        mental_activity_articles = []
        operation_manager.set_db_connection()

        if request.method == 'POST':
            article = Article(
                title=request.form.get('title', None),
                description=request.forphysicalm.get('description', None),
                category='mental'
            )

            query = query_manager.make_insert_query(article, 'articles')
            print('Query: ', query)
            res = operation_manager.execute_query(query)
            print('DB response: ', res)
        
        query = query_manager.make_get_query('articles', 'mental_activities')
        res = operation_manager.execute_query(query)
        operation_manager.close_db_connection()
        for item in res:
            # TODO add error handling when building articles
            article = Article(id=item[0], title=item[1], description=item[2], category=item[3])
            mental_activity_articles.append(article)
        
        # print('Physical activity articles: ', mental_activity_articles)
        return render_template('mental_activities.html', articles=mental_activity_articles)
    
    @app.route('/mental_activities/<article_id>')
    def show_mind_article(article_id):
        '''
        Load the respective mental activities article page:
        - load the mental activities article
        - make a list of available mental activity articles
        '''
        articles = []
        data = {
            'articles': articles
        }
        operation_manager.set_db_connection()

        if request.method == 'PUT':
            article = Article(
                id=request.form['id'],
                title=request.form['title'],
                description=request.form['description'],
                category=request.form['category']
            )

            query = query_manager.make_update_query_by_id(article, 'articles')
            print('Query: ', query)
            res = operation_manager.execute_query(query)
            print('DB response: ', res)

        elif request.method == 'DELETE':
            article = Article(
                id=request.form['id'],
                title=request.form['title'],
                description=request.form['description'],
                category=request.form['category']
            )

            query = query_manager.make_remove_query_id(article, 'articles')
            print('Query: ', query)
            res = operation_manager.execute_query(query)
            print('DB response: ', res)

            return url_for('/mental_activities')
        
        query = query_manager.make_get_query('articles', 'mental_activity')
        res = operation_manager.execute_query(query)
        operation_manager.close_db_connection()
        for item in res:
            # TODO add error handling when building articles
            article = Article(id=item[0], title=item[1], description=item[2], category=item[3])
            if article.id == article_id:
                data['current_article'] = article
            else:
                articles.append(article)

        return render_template('mental_activities_article.html', data=data)

    return app