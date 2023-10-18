"""
ASGI config for project_video_chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import app_video_chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_video_chat.settings')

django_asgi_app = get_asgi_application()  # Get the default Django ASGI application

application = ProtocolTypeRouter({
    "http": django_asgi_app,  # Use the default Django ASGI app for HTTP requests
    "websocket": AuthMiddlewareStack(
        URLRouter(
            app_video_chat.routing.websocket_urlpatterns
        )
    ),
})