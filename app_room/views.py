from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import *

@login_required
def rooms(request):
    rooms = Room.objects.all()
    
    return render(request, 'app_room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]
    
    return render(request, 'app_room/room.html', {'room': room}, {'messages': messages})