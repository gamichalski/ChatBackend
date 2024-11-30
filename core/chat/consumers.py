import json
from .models import Chat, ChatMessage
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = self.scope["url_route"]["kwargs"]["room_name"]

        # Get or Create the actual chat
        self.chat_group, _ = await sync_to_async(Chat.objects.get_or_create)(chat_name=self.room_group_name)

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
            user_type = data_json.get('user_type', 1)
            user = data_json.get('user', None)


            if user_type == 1:
                await sync_to_async(Chat.objects.filter(chat_name=self.room_group_name).update)(user=user)


            # Creating the message registry
            message = await sync_to_async(ChatMessage.objects.create)(
                author_type = user_type,
                body = message_body,
                chat = self.chat_group
            )

            # Send message
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "chat_message", "body": message_body, 'user_type': user_type, 'user': user}
            )

        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")

    # Handler to deal with the messages
    async def chat_message(self, event):
        body = event["body"]
        user_type = event["user_type"]
        user = event["user"]

        await self.send(text_data=json.dumps({'body': body, 'user_type': user_type, 'user': user}))