from flask import Blueprint
Product = Blueprint('Product',__name__)

from . import ProductAPI
