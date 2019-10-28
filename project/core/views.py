import requests
from rest_framework.response import Response
from rest_framework.views import APIView


API_URL = "https://api.spacexdata.com/v3/launches/"
NEXT = "next"
LATEST = "latest"
UPCOMING = "upcoming"
PAST = "past"


class Launches(APIView):
    """
        Returns a list of SpaceX launches, scheduled and made.
    """

    @staticmethod
    def get(self):
        launches = requests.get(API_URL)
        return Response(launches.json())


class NextLaunch(APIView):
    """
        Returns information from the next launche of SpaceX.
    """

    @staticmethod
    def get(self):
        next_l = requests.get("{}{}".format(API_URL, NEXT))
        return Response(next_l.json())


class UpcomingLaunch(APIView):
    """
        Returns information containing upcoming planned launches of SpaceX.
    """

    @staticmethod
    def get(self):
        upcoming = requests.get("{}{}".format(API_URL, UPCOMING))
        return Response(upcoming.json())


class LatestLaunch(APIView):
    """
        Returns information from the latest SpaceX launche.
    """

    @staticmethod
    def get(self):
        latest = requests.get("{}{}".format(API_URL, LATEST))
        return Response(latest.json())


class PastLaunch(APIView):
    """
        Returns information from the previous SpaceX launches.
    """

    @staticmethod
    def get(self):
        past = requests.get("{}{}".format(API_URL, PAST))
        return Response(past.json())
