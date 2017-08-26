# coding: utf-8
from flask import jsonify,Response,request
import json
from . import api
@api.route('/api1/',methods = ['POST'])
def api1():
    key1=request.get_json().get(Type)
    key2=request.get_json().get(Type)
@api.route('/api2/?arg2=type&arg3=type&arg1=type',methods = ['GET'])
def api2(arg2,arg3,arg1):
