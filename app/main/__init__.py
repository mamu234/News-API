from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevConfig
from app import views
from app import error




bootstrap = Bootstrap()

app = Flask(__name__,relative_config = True)
  

    # Creating the app configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')



    # Initializing flask extensions
bootstrap.init_app(app)

    
# app.register_blueprint(main_blueprint)
# configure_request(app)
# return app
 
    