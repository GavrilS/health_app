import os
from flask import (
    Flask, render_template, url_for
)

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/nutrition')
    def show_nutrition_category():
        return render_template('nutrition.html')
    
    @app.route('/nutrition/<article_id>')
    def show_nutrition_article(article_id):
        return f'Opening nutrition article with id {article_id}'
    
    @app.route('/physical')
    def show_physical_category():
        return render_template('physical.html')
    
    @app.route('/physical/<article_id>')
    def show_physical_article(article_id):
        return f'Opening physical article with id {article_id}'
    
    @app.route('/mind')
    def show_mind_category():
        return render_template('mind.html')
    
    @app.route('/mind/<article_id>')
    def show_mind_article(article_id):
        return f'Opening mind article with id {article_id}'

    return app