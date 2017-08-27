# coding: utf-8
from flask import jsonify,Response,request
import json
from . import api

#@login_required
@api.route('/api4/',methods = ['POST'])
def api4():
    key2=request.get_json().get('key2')
    key1=request.get_json().get('key1')
    return Response(json.dumps({
        "key2":"content",
        "key1":"content",
        }))
    pass
