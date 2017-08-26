# coding: utf-8
from flask import jsonify,Response,request
import json
from . import api

#@edit_required
@api.route('/api3/',methods = ['PUT'])
def api3():
    key1=request.get_json().get('key1')
    key2=request.get_json().get('key2')
    return Response(json.dumps({
        "key1":"content",
        "key2":"content",
        }))
        }))
    pass
