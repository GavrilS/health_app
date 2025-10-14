import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello World!'
    
    @app.route('/nutrition')
    def show_nutrition_category():
        return 'Nutrition'
    
    @app.route('/nutrition/<article_id>')
    def show_nutrition_article(article_id):
        return f'Opening nutrition article with id {article_id}'
    
    @app.route('/physical')
    def show_physical_category():
        return 'Physical'
    
    @app.route('/physical/<article_id>')
    def show_physical_article(article_id):
        return f'Opening physical article with id {article_id}'
    
    @app.route('/mind')
    def show_mind_category():
        return 'Mind'
    
    @app.route('/mind/<article_id>')
    def show_mind_article(article_id):
        return f'Opening mind article with id {article_id}'

    return app