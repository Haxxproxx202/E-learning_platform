# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.generic.websocket import WebsocketConsumer
# from asgiref.sync import async_to_sync
# from django.utils import timezone
#
#
# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.user = self.scope['user']
#         self.id = self.scope['url_route']['kwargs']['course_id']
#         self.room_group_name = 'chat_%s' % self.id
#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )
#         await self.accept()
#
#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )
#
#     async def receive(self, text_data=None, bytes_data=None):
#         if text_data:
#             text_data_json = json.loads(text_data)
#             message = text_data_json['message']
#             now = timezone.now()
#             await self.channel_layer.group_send(
#                 self.room_group_name,
#                 {
#                     'type': 'chat_message',
#                     'message': message,
#                     'user': self.user.username,
#                     'datetime': now.isoformat()
#                 }
#             )
#         else:
#             pass
#
#     async def chat_message(self, event):
#         await self.send(text_data=json.dumps(event))

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
from .models import Message


from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
from .models import Message


from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.id = self.scope['url_route']['kwargs']['course_id']
        self.room_group_name = 'chat_%s' % self.id

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Pobranie historii wiadomości i wysłanie do klienta
        message_history = await self.get_message_history()
        for message in message_history:
            await self.send(text_data=json.dumps(message))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            text_data_json = json.loads(text_data)
            message = text_data_json['message']

            await self.save_message(message)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'user': self.user.username
                }
            )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    @database_sync_to_async
    def save_message(self, message):
        Message.objects.create(content=message, user=self.user, course_id=self.id)

    @database_sync_to_async
    def get_message_history(self):
        messages = Message.objects.filter(course_id=self.id)
        message_history = []
        for message in messages:
            message_data = {
                'type': 'chat_message',
                'message': message.content,
                'user': message.user.username
            }
            message_history.append(message_data)
        return message_history
