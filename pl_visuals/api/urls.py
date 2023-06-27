from django.urls import path
from . import views

urlpatterns = [
    path("club/", views.club_list_create_view),
    path("club/<int:pk>/", views.club_detail_view),
    path("match/", views.match_list_create_view),
    path("match/<int:pk>/", views.match_detail_view),
    path("league/", views.league_data_list_create_view),
    path("league/<int:pk>/", views.league_data_detail_view),
    path("competition/", views.competition_data_list_create_view),
    path("competition/<int:pk>/", views.competition_data_detail_view),
]
