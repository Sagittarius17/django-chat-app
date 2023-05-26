from django.urls import path
from . import views

urlpatterns = [
    path('room/', views.video_chat_room, name='video_chat_room'),
]
