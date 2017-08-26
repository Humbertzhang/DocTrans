# coding: utf-8
from flask import jsonify,Response,request
import json
from . import api
@api.route('/api3/',methods = ['PUT'])
def api3():
    key1=request.get_json().get(Type)
    key2=request.get_json().get(Type)
