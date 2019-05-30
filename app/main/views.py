# -*- coding: utf-8 -*-

from . import main
from flask import jsonify, request, make_response, session
from app.application import db, mongo
from bson import json_util, ObjectId
from datetime import timedelta

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
    data = mongo.db.ttcc1.find().limit(5)
    tmp = list(data)
    page_sanitized = json.loads(json_util.dumps(tmp))
    return jsonify({
        'data': page_sanitized
    })


@main.route('/getcookie')
def get_cookie():
    user_id = session.get('user_id')
    return user_id
