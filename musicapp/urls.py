from django.urls import path
from .views import artiste_list, song_list, song_details

urlpatterns = [
    path('artiste/', artiste_list),
    path('song/',  song_list),
    path('song/<int:id>/', song_details)
]