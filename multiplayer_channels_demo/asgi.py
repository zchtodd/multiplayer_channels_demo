import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from channels_demo.routing import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "multiplayer_channels_demo.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(websocket_urlpatterns),
    }
)
