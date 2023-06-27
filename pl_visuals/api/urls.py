from django.urls import path
from . import views

urlpatterns = [
    path("league/", views.league_data_list_create_view),
    path("league/<int:pk>/", views.league_data_detail_view),
    path("competition/", views.competition_data_list_create_view),
    path("competition/<int:pk>/", views.competition_data_detail_view),
]
