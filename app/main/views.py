# -*- coding: utf-8 -*-

from . import main
from flask import jsonify, request, session, logging
from app.database import MongoDB
from bson import json_util

import logging
import uuid
import json


@main.before_request
def check_user():
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid1())


@main.route('/')  # 注意這裡是 main.route 而不再是 app.route
@main.route('/index')
def index():
    return jsonify({
        'data': "Hello"
    })


@main.route('/test')
def testMongo():
    if MongoDB.Insert('test', {'test': '1'}) == False:
        logging.error("Can't Insert Data to Mongo. ")
    return jsonify({
        'status': 'OK'
    })
