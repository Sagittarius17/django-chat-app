import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message  # Assuming you have a Message model in models.py

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Assuming you have a Message model with a 'content' field
        Message.objects.create(content=message)

        # Send the message back to the client
        await self.send(text_data=json.dumps({
            'message': message
        }))