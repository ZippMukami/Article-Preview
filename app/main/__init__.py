from flask import Blueprint, Flask
from pip import main
main = Blueprint('main',__name__)
from . import view, errors







# from ensurepip import bootstrap
# from flask import Flask
# from .config import DevConfig
# from flask_bootstrap import Bootstrap

# #Initializing application
# app = Flask(__name__, instance_relative_config = True)


# # setting up configuration 
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')

# # Initializing flask extensions
# bootstrap = Bootstrap(app)

# from app import views
# from app import error