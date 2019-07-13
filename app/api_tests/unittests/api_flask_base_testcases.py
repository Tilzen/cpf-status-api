from json import loads
from unittest import TestCase
from app import create_app
from flask import url_for


class TestAPIBase(TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.user = {
            'username': 'test',
            'password': '1234'
        }

    def tearDown(self):
        self.app.db.drop_all()

    def create_user(self):
        self.client.post(url_for('user.register'), json=self.user)

    def create_token(self):
        login = self.client.post(url_for('login.login'), json=self.user)
        return {
            'Authorization':
                'Bearer ' + loads(login.data.decode())['access_token']
                }
