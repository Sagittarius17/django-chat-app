from django.shortcuts import render
# Create your views here.

from .models import *  # Import the Message model

def index_view(request):
    # Retrieve all messages from the Message model
    messages = Message.objects.all()
    username = User.name
    # Pass the messages and username to the template context
    context = {
        'messages': messages,
        'username': username,
    }

    # Render the template with the context
    return render(request, 'BartaText/base.html', context)

