"""
ASGI config for coding_challenges project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os


from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import ascii_cam.routing
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coding_challenges.settings")

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            ascii_cam.routing.websocket_urlpatterns
        )
    )
})

# application = get_asgi_application()
