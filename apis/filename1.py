# coding: utf-8
from flask import jsonify,Response,request
import json
from . import api

#@admin_required
@api.route('/api1/',methods = ['POST'])
def api1():
    key1=request.get_json().get('key1')
    key2=request.get_json().get('key2')
    return Response(json.dumps({
        "key1":"content",
        "key2":"content",
        }))
    pass

@api.route('/api2/?arg2=type&arg1=type&arg3=type',methods = ['GET'])
def api2(arg2,arg1,arg3):
    return Response(json.dumps({
        "key1":"content",
        "key2":"content",
        }))
    pass
