from django.urls import path

from .views import Launches, NextLaunch, UpcomingLaunch, LatestLaunch, PastLaunch

urlpatterns = [
    path("", Launches.as_view()),
    path("next", NextLaunch.as_view()),
    path("upcoming", UpcomingLaunch.as_view()),
    path("latest", LatestLaunch.as_view()),
    path("past", PastLaunch.as_view()),
]
