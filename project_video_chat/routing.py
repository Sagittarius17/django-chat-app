from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from app_video_chat import consumers  # Adjust the import based on your project structure

websocket_urlpatterns = [
    path('ws/videocall/<str:room_name>/', consumers.VideoCallConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "websocket": URLRouter(websocket_urlpatterns),
})
