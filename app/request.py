from app import app
import urllib.request, json
from .models import bulletin

#Getting api key
api_key = app.config['BULLETIN_API_KEY']

#Getting the bulletin base url
base_url = app.config["BULLETIN_API_BASE_URL"]