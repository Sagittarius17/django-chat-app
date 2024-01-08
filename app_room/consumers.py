import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from .models import *

# WebSocket consumer class for handling chat functionality
class ChatConsumer(AsyncWebsocketConsumer):
    # Method triggered when a WebSocket connection is established
    async def connect(self):
        # Get the room name from the URL route
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # Create a unique group name for the room
        self.room_group_name = 'chat_%s' % self.room_name
        
        # Add the consumer to the group associated with the room
        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name
        )
        
        # Accept the WebSocket connection
        await self.accept()
        
    # Method triggered when a WebSocket connection is closed
    async def disconnect(self, close_code):
        # Remove the consumer from the group associated with the room
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
    # Method triggered when the consumer receives a message from the WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        # Parse the received JSON data
        data = json.loads(text_data)
        print(f"data {data}")
        # Extract message details from the received data
        message = data['message']
        username = data['username']
        room = data['room']
        timestamp = timezone.now()
        
        # Save the message to the database
        await self.save_message(username, room, message)
        
        # Send the message to the group associated with the room
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'room': room,
                'timestamp': timestamp.isoformat(),  # Convert to ISO 8601 format

            }
        )
        
    # Method triggered when a message is received from the group
    async def chat_message(self, event):
        # Extract message details from the event
        message = event['message']
        username = event['username']
        room = event['room']
        timestamp = event['timestamp']
        
        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'room': room,
            'timestamp': timestamp,
        }))
        
    # Method to save a message to the database (using sync_to_async to call synchronous code)
    @sync_to_async
    def save_message(self, username, room, message):
        # Retrieve user and room objects from the database
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)
        
        # Create a new message object and save it to the database
        Message.objects.create(user=user, room=room, content=message)
