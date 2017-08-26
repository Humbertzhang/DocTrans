# coding: utf-8
from flask import jsonify,Response,request
import json
from . import api
@api.route('/api5/',methods = ['OTHER'])
def api5():
