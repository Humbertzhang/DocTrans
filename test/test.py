import unittest
from app import create_app
from flask import current_app,url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
import random
import json
import base64

db = SQLAlchemy()
class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exits(self):
        self.assertFalse(current_app is None)


    def test_rank_api1(self):
        response = self.client.post(),
            url_for('api.api1',_external=True),
            headers = { },
            data=json.dumps({
                "key2":"content"
                "key1":"content",
            }),
            content_type = 'application/json')
    def test_rank_api2(self):
        response = self.client.get(arg1=value,arg2=value,arg3=value),
            url_for('api.api2',_external=True),
            content_type = 'application/json')
    def test_rank_api3(self):
        response = self.client.put(),
            url_for('api.api3',_external=True),
            headers = { },
            data=json.dumps({
                "key2":"content"
                "key1":"content",
            }),
            content_type = 'application/json')
    def test_rank_api4(self):
        response = self.client.post(),
            url_for('api.api4',_external=True),
            headers = { },
            data=json.dumps({
                "key2":"content"
                "key1":"content",
            }),
            content_type = 'application/json')
    def test_rank_api5(self):
        response = self.client.delete(),
            url_for('api.api5',_external=True),
            headers = { },
            content_type = 'application/json')
