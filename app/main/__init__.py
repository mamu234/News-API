from json.tool import main
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask import Blueprint
from  main import views
from app.main import main_blueprint

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    main = Blueprint('main',__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    
    app.register_blueprint(main_blueprint)
    return app

    