from flask import Flask
from flask_bootstrap import Bootstrap
from .config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

# Initializing application
    app = Flask(__name__)

    # creating the app configuration
    app.config.from_object(DevConfig[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)


    return app
