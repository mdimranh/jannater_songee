from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer

class NotificationConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['id']
        self.room_group_name = 'notification_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()



    def receive(self, text_data):
        pass

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def send_notification(self, event):
        data = json.loads(event.get('value'))
        self.send(text_data = json.dumps({'notification': data}))


