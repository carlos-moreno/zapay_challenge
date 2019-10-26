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
        Returns the list of all SpaceX releases, both those that have already happened and those that are scheduled to happen. [see here][ref].

        [ref]: https://docs.spacexdata.com/?version=latest#5fc4c846-c373-43df-a10a-e9faf80a8b0a
    """

    def get(self, request):
        l = requests.get(API_URL)
        return Response(l.json())


class NextLaunch(APIView):
    """
        Return the next launch of SpaceX. [see here][ref].

        [ref]: https://docs.spacexdata.com/?version=latest#c75a20cf-50e7-4a4a-8856-ee729e0d3868
    """

    def get(self, request):
        nl = requests.get("{}{}".format(API_URL, NEXT))
        return Response(nl.json())


class UpcomingLaunch(APIView):
    """
        Return the upcoming launches of SpaceX. [see here][ref].

        [ref]: https://docs.spacexdata.com/?version=latest#e001c501-9c09-4703-9e29-f91fbbf8db7c
    """

    def get(self, request):
        nl = requests.get("{}{}".format(API_URL, UPCOMING))
        return Response(nl.json())


class LatestLaunch(APIView):
    """
        Return the latest launch of SpaceX. [see here][ref].

        [ref]: https://docs.spacexdata.com/?version=latest#07a29989-38e3-47fb-9f64-c132b5842ff0
    """

    def get(self, request):
        nl = requests.get("{}{}".format(API_URL, LATEST))
        return Response(nl.json())


class PastLaunch(APIView):
    """
        Return the past launches of SpaceX. [see here][ref].

        [ref]: https://docs.spacexdata.com/?version=latest#fce450d6-e064-499a-b88d-34cc22991bcc
    """

    def get(self, request):
        nl = requests.get("{}{}".format(API_URL, PAST))
        return Response(nl.json())
