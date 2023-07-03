from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("team/<int:id>/", views.teams, name="team"),
]
