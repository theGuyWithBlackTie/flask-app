from flask import Flask
import os

app = Flask(__name__)
app.config.from_pyfile('app_config.py')

from server import routes
from server import config

# creating strage directory is doesn't exists
if not os.path.isdir(app.config[config.UPLOAD_FOLDER]):
    os.makedirs(app.config[config.UPLOAD_FOLDER])
