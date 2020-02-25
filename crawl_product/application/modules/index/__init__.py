from flask import Blueprint
from application import db
index = Blueprint("index", __name__, template_folder="templates", static_folder="static")

from .views import *



















