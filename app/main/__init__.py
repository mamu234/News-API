from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevConfig
from flask import Blueprint

from app.main import main_blueprint
from templates.requests import configure_request

bootstrap = Bootstrap()

app = Flask(__name__,relative_config = True)
    # main = Blueprint('main',__name__)

    # Creating the app configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app.models import views

    # Initializing flask extensions
bootstrap.init_app(app)

    
# app.register_blueprint(main_blueprint)
# configure_request(app)
# return app
 
    