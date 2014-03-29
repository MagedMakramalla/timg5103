from flask import Flask
import logging

server = Flask(__name__)
server.config.from_pyfile('config.py')

import app

@server.route('/')
def hello_world():
    return app.hello()


@server.route('/find')
def find_connection():
    return app.find_connection()
