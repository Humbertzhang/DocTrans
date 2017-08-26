#coding:utf-8
"""
Static content for test
"""
static_test_content = [
    "import unittest\n",
    "from flask import create_app\n",
    "from flask_sqlalchemy import SQLAlchemy\n",
    "import random\n",
    "import json\n",
    "import base64\n\n\n",
    "Class BasicTestCase(unittest.TestCase):\n\n",
    " "*4 + "def setUp(self):\n",
    " "*8 + "self.app = create_app()\n",
    " "*8 + "self.app_context = self.app.app_context()\n",
    " "*8 + "self.app_context.push()\n",
    " "*8 + "self.client = self.app.test_client()\n",
    " "*8 + "db.create_all()\n\n",
    " "*4 + "def tearDown(self):\n",
    " "*8 + "db.session.remove()\n",
    " "*8 + "db.drop_all()\n",
    " "*8 + "self.app_context.pop()\n\n",
    " "*4 + "def test_app_exits(self):\n",
    " "*8 + "self.assertFalse(current_app is None)\n\n\n",
]