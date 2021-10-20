from flask import Flask
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

app.config.from_pyfile('config.py')
from App import routes


def get_app():
    return app