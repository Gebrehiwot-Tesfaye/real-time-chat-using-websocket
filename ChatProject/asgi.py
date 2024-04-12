import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels import DEFAULT_CHANNEL_LAYER   # Importing DEFAULT_CHANNEL_LAYER

# Import your routing configuration from the app
from ChatApp import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChatProject.settings')

# Get the Django ASGI application
django_asgi_app = get_asgi_application()

# Define the ASGI application for WebSocket connections
application = ProtocolTypeRouter({
    "http": django_asgi_app,  # For standard HTTP requests
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})

