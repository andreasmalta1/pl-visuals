from django.urls import path
from . import views

urlpatterns = [
    path("club1/", views.league_data_list_create_view),
    path("club1/<int:pk>/", views.league_data_detail_view),
    path("match/", views.league_data_list_create_view),
    path("match/<int:pk>/", views.league_data_detail_view),
    path("league/", views.league_data_list_create_view),
    path("league/<int:pk>/", views.league_data_detail_view),
    path("competition/", views.competition_data_list_create_view),
    path("competition/<int:pk>/", views.competition_data_detail_view),
]
