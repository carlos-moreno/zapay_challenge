from django.test import TestCase
from django.shortcuts import resolve_url as r


class EndPointApiTest(TestCase):

    def setUp(self):
        self.response = self.client.get("http://127.0.0.1:8000/v1/")

    def test_get(self):
        """GET /v1 must return status code 200"""
        self.assertEqual(200, self.response.status_code)
