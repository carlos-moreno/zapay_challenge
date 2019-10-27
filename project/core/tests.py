from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):

    def setUp(self):
        self.response = self.client.get(r("home"))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)


class EndPointNextTest(TestCase):

    def setUp(self):
        self.response = self.client.get(r("next"))

    def test_get(self):
        """GET /v1/next must return status code 200"""
        self.assertEqual(200, self.response.status_code)


class EndPointUpcomingTest(TestCase):

    def setUp(self):
        self.response = self.client.get(r("upcoming"))

    def test_get(self):
        """GET /v1/upcoming must return status code 200"""
        self.assertEqual(200, self.response.status_code)


class EndPointLatestTest(TestCase):

    def setUp(self):
        self.response = self.client.get(r("latest"))

    def test_get(self):
        """GET /v1/latest must return status code 200"""
        self.assertEqual(200, self.response.status_code)


class EndPointPastTest(TestCase):

    def setUp(self):
        self.response = self.client.get(r("past"))

    def test_get(self):
        """GET /v1/past must return status code 200"""
        self.assertEqual(200, self.response.status_code)
