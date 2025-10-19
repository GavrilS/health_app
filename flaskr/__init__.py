import os
from flask import (
    Flask, render_template, url_for
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
    
    @app.route('/nutrition')
    def show_nutrition_category():
        '''
        Load the nutrition category page:
        - pull all nutrition articles from db
        - make a list of titles to display as links to separate articles
        - populate the list on the page
        '''
        query = query_manager.make_get_query('articles', 'nutrition')
        print('*'*80)
        print('Nutrition get query: ', query)
        print('*'*80)
        res = operation_manager.execute_query(query)
        print('Res pre-close: ', res)
        operation_manager.close_db_connection()
        return render_template('nutrition.html')
    
    @app.route('/nutrition/<article_id>')
    def show_nutrition_article(article_id):
        '''
        Load the respective nutrition article page:
        - no extra data needs to be loaded
        '''
        return f'Opening nutrition article with id {article_id}'
    
    @app.route('/physical')
    def show_physical_category():
        '''
        Load the physical activities category page:
        - pull all physical activity articles from db
        - make a list of titles to display as links to separate articles
        - populate the list on the page
        '''
        return render_template('physical.html')
    
    @app.route('/physical/<article_id>')
    def show_physical_article(article_id):
        '''
        Load the respective physical activities article page:
        - no extra data needs to be loaded
        '''
        return f'Opening physical article with id {article_id}'
    
    @app.route('/mind')
    def show_mind_category():
        '''
        Load the mental activities category page:
        - pull all mental activity articles from db
        - make a list of titles to display as links to separate articles
        - populate the list on the page
        '''
        return render_template('mind.html')
    
    @app.route('/mind/<article_id>')
    def show_mind_article(article_id):
        '''
        Load the respective mental activities article page:
        - no extra data needs to be loaded
        '''
        return f'Opening mind article with id {article_id}'

    return app