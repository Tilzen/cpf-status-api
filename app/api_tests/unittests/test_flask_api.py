from unittest import TestCase
from flask import url_for
from .api_flask_base_testcases import TestAPIBase


class TestDocumentation(TestAPIBase):
    def test_documentation_should_return_200(self):
        response = self.client.get(url_for('cpf_authentication.index'))
        self.assertEqual(response.status_code, 200)


class TestCPFSituation(TestAPIBase):
    def test_get_cpf_should_return_200(self):
        self.create_user()
        token = self.create_token()
        cpf_example = '40442820135'
        response = self.client.get(f'/consult/{cpf_example}', headers=token)
        self.assertEqual(response.status_code, 200)

    def test_get_cpf_should_return_error(self):
        self.create_user()
        token = self.create_token()
        cpf_example = '40442820137'
        response = self.client.get(f'/consult/{cpf_example}', headers=token)
        self.assertIn(b'error', response.data)

    def test_get_cpf_should_return_jwt_message(self):
        self.create_user()
        token = self.create_token()
        cpf_example = '40442820137'
        response = self.client.get(f'/consult/{cpf_example}')
        self.assertIn(b'msg', response.data)
