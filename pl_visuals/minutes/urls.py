from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:id>/", views.teams, name="team"),
    path("<int:id>/league/<int:season>/", views.league_graph, name="league_graph"),
    path("<int:id>/comp/<int:season>/", views.comp_graph, name="comp_graph"),
]
