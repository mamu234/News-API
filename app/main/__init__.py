from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevConfig
from app import views
from app import error
from config import config_options
from flask import Blueprint
from  templates.requests import configure_request





bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__,relative_config = True)
  
    app.config.from_object(config_options[config_name])
    # Creating the app configurations
    app.config.from_object(DevConfig)
    app.config.from_pyfile('config.py')



# Initializing flask extensions
    bootstrap.init_app(app)

# configure_request(app)
    
    app.register_blueprint(main_blueprint)
    from app.main import main as main_blueprint
    
    configure_request(app)


    return app
 
    