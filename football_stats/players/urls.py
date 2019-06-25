from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='players'),
    path('player_upload', views.player_upload, name='player_upload'),
    path('delete_club/<str:club>/', views.player_club_delete, name='player_club_delete'),
    path('delete_league/<str:league>/', views.player_league_delete, name='player_league_delete'),
    path('player_upload/delete', views.player_delete, name='player_delete'),
]