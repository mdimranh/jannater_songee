
import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from .routing import ws_patterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jannatersongee.settings')

application = get_asgi_application()

application = ProtocolTypeRouter({
    'websocket': URLRouter(ws_patterns)
})
