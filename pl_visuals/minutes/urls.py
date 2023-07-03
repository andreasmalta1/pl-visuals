from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("team/<int:id>/", views.teams, name="team"),
    path("team/<int:id>/league", views.league_graph, name="league_graph"),
    path("team/<int:id>/competition", views.comp_graph, name="comp_graph"),
]
