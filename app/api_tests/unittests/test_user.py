from flask import url_for
from .api_flask_base_testcases import TestAPIBase


class TestBlueprintUser(TestAPIBase):
    def test_api_should_register_the_user(self):
        response = self.client.post(url_for('user.register'), json=self.user)
        self.assertEqual(response.status_code, 201)

    def test_api_dont_should_register_the_user(self):
        user = {"username": "test"}
        response = self.client.post(url_for('user.register'), json=user)
        self.assertEqual(response.status_code, 401)
