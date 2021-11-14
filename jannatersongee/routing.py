from django.urls import path
from biodata.consumers import *

ws_patterns = [
    path('ws/notification/<id>', NotificationConsumer.as_asgi()),
]