# coding: utf-8
from flask import jsonify,Response,request
import json
from . import api

#@admin_required
@api.route('/api1/',methods = ['POST'])
def api1():
    key2=request.get_json().get('key2')
    key1=request.get_json().get('key1')
    return Response(json.dumps({
        "key2":"content",
        "key1":"content",
        }))
    pass

@api.route('/api2/?arg3=type&arg1=type&arg2=type',methods = ['GET'])
def api2(arg3,arg1,arg2):
    return Response(json.dumps({
        "key2":"content",
        "key1":"content",
        }))
    pass
