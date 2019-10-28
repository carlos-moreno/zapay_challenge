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

        Parameters that can be passed in querystring:
            - flight_number
            - launch_year
            - launch_date_utc

        For more parameter information and API details, see here:
        [ref]: https://docs.spacexdata.com/?version=latest#5fc4c846-c373-43df-a10a-e9faf80a8b0a
    """

    def get(self, request):
        l = requests.get(API_URL)
        return Response(l.json())


class NextLaunch(APIView):
    """
        Returns information from the next launchec of SpaceX.
    """

    def get(self, request):
        nl = requests.get("{}{}".format(API_URL, NEXT))
        return Response(nl.json())


class UpcomingLaunch(APIView):
    """
        Returns information containing upcoming planned launches of SpaceX.

        Parameters that can be passed in querystring:
            - flight_number
            - launch_year
            - launch_date_utc

        For more parameter information and API details, see here:
        [ref]: https://docs.spacexdata.com/?version=latest#e001c501-9c09-4703-9e29-f91fbbf8db7c
    """

    def get(self, request):
        nl = requests.get("{}{}".format(API_URL, UPCOMING))
        return Response(nl.json())


class LatestLaunch(APIView):
    """
        Returns information from the latest SpaceX launche.
    """

    def get(self, request):
        nl = requests.get("{}{}".format(API_URL, LATEST))
        return Response(nl.json())


class PastLaunch(APIView):
    """
        Returns information from the previous SpaceX launches.

        Parameters that can be passed in querystring:
            - flight_number
            - launch_year
            - launch_date_utc

        For more parameter information and API details, see here:
        [ref]: https://docs.spacexdata.com/?version=latest#fce450d6-e064-499a-b88d-34cc22991bcc
    """

    def get(self, request):
        nl = requests.get("{}{}".format(API_URL, PAST))
        return Response(nl.json())
