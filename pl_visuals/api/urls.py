from django.urls import path
from . import views

urlpatterns = [
    path("club/", views.club_list_create_view),
    path("club/<int:pk>/", views.club_detail_view),
    path("league/", views.league_list_create_view),
    path("league/<int:pk>/", views.league_detail_view),
    path("match/", views.match_list_create_view),
    path("match/<int:pk>/", views.match_detail_view),
    path("match/update/<int:pk>/", views.match_update_view),
    path("league-data/", views.league_data_list_create_view),
    path("league-data/<int:pk>/", views.league_data_detail_view),
    path("league-data/update/<int:pk>/", views.league_data_update_view),
    path("competition-data/", views.competition_data_list_create_view),
    path("competition-data/<int:pk>/", views.competition_data_detail_view),
    path("competition-data/update/<int:pk>/", views.competition_data_update_view),
]
