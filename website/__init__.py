import os
from dotenv import load_dotenv
from flask import Flask


def create_app():
    app = Flask(__name__)

    load_dotenv('.env')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
