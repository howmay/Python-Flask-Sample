# -*- coding: utf-8 -*-

from . import Product
from flask import jsonify, request, session, logging
from app.database import MongoDB
from bson import json_util

import logging
import uuid
import json

@Product.before_request
def check_user():
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid1())


@Product.route('/')  # 注意這裡是 main.route 而不再是 app.route
@Product.route('/index')
def index():
    return jsonify({
        'data': "Hello"
    })

@Product.route('/ProductAPI/GetAllProduct')
def GetAllProduct():
    return jsonify({
        'id':'product1',
        'Name':'Willy'
    })

@Product.route('/test')
def testMongo():
    if MongoDB.Insert('test', {'test': '1'}) == False:
        logging.error("Can't Insert Data to Mongo. ")
    return jsonify({
        'status': 'OK'
    })
