"""
WSGI config for ChatProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

"""
ASGI config for ChatProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_wsgi_application
from ChatApp import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChatProject.settings')

django_wsgi_app = get_wsgi_application()

application = ProtocolTypeRouter({
    "http": django_wsgi_app,
    "websocket": URLRouter(
        routing.websocket_urlpatterns
    )
}) 
