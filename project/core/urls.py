from django.urls import path

from .views import Launches, NextLaunch, UpcomingLaunch, LatestLaunch, PastLaunch

urlpatterns = [
    path("next", NextLaunch.as_view(), name="next"),
    path("upcoming", UpcomingLaunch.as_view(), name="upcoming"),
    path("latest", LatestLaunch.as_view(), name="latest"),
    path("past", PastLaunch.as_view(), name="past"),
]
