# coding: utf-8
from flask import jsonify,Response,request
import json
from . import api

#@edit_required
@api.route('/api3/',methods = ['PUT'])
def api3():
    key2=request.get_json().get('key2')
    key1=request.get_json().get('key1')
    return Response(json.dumps({
        "key2":"content",
        "key1":"content",
        }))
    pass
