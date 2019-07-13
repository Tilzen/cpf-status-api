from flask import url_for
from .api_flask_base_testcases import TestAPIBase


class TestLogin(TestAPIBase):
    def test_should_generate_a_token(self):
        self.create_user()
        login = self.client.post(url_for('login.login'), json=self.user)
        expected = ['access_token', 'message', 'refresh_token']
        response = list(login.json.keys())
        self.assertEqual(response, expected)

    def test_api_dont_should_login_user_with_error(self):
        user = {"username": "test"}
        login = self.client.post(url_for('login.login'), json=user)
        expected = ['error']
        response = list(login.json.keys())
        self.assertEqual(response, expected)
