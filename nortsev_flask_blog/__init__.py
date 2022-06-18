from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from nortsev_flask_blog.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    login_manager.init_app(app)

    from nortsev_flask_blog.main.views import main
    app.register_blueprint(main)
    
    return app