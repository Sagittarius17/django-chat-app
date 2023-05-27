from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_layout, name='mainLayout'),
    path('room/', views.video_chat_room, name='videoChatRoom'),
]
