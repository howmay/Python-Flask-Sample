# -*- coding: utf-8 -*-

#from config import Config

from flask import Flask, render_template
from flask_pymongo import PyMongo

import os

mongo = PyMongo()


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/test"

    mongo.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    app.config['SECRET_KEY'] = os.urandom(24)

    # from .middleware import Middleware
    # app.wsgi_app = Middleware(app.wsgi_app)

    return app
