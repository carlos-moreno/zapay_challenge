from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LauncheSerializer
import json
import requests

# Create your views here.
API_URL = 'https://api.spacexdata.com/v3/launches/'
NEXT = 'next'
LATEST = 'latest'
UPCOMING = 'upcoming'
PAST = 'past'


class Launches(APIView):
    def get(self, request):
        l = requests.get(API_URL)
        return Response(l.json())


class NextLaunch(APIView):
    def get(self, request):
        nl = requests.get('{}{}'.format(API_URL, NEXT))
        return Response(nl.json())


class UpcomingLaunch(APIView):
    def get(self, request):
        nl = requests.get('{}{}'.format(API_URL, UPCOMING))
        return Response(nl.json())


class LatestLaunch(APIView):
    def get(self, request):
        nl = requests.get('{}{}'.format(API_URL, LATEST))
        return Response(nl.json())


class PastLaunch(APIView):
    def get(self, request):
        nl = requests.get('{}{}'.format(API_URL, PAST))
        return Response(nl.json())
