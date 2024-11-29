import json
from .models import Chat, ChatMessage
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.room_group_name = self.scope["url_route"]["kwargs"]["room_name"]

        print(self.user)

        if not self.user.is_authenticated:
            await self.close()
            return

        # Get or Create the actual chat
        self.chat_group, created = await sync_to_async(Chat.objects.get_or_create)(chat_name=self.room_group_name)
        if created:
            self.chat_group.user = self.user.id
            await sync_to_async(self.chat_group.save)()

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        try:
            data_json = json.loads(text_data)
            message_body = data_json.get('body', None)
            user_type = data_json.get('user_type', 'USER')

            # Creating the message registry
            message = ChatMessage.objects.create(
                author_type = user_type,
                body = message_body,
                chat = self.chat_group
            )
            message.save()

            # Send message
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "chat_message", "body": message_body, 'user_type': user_type}
            )

        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")

    # Handler to deal with the messages
    async def chat_message(self, event):
        body = event["body"]
        user_type = event["user_type"]

        await self.send(text_data=json.dumps({'body': body, 'user_type': user_type}))