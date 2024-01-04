from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib import messages as msg
from .models import *

@login_required
def rooms(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    
    return render(request, 'app_room/rooms.html', context)

@login_required
# def room(request, slug):
#     room = Room.objects.get(slug=slug)
#     messages = Message.objects.filter(room=room)[0:25]
    
#     return render(request, 'app_room/room.html', {'room': room}, {'messages': messages})

def room(request, slug):
    try:
        room = get_object_or_404(Room, slug=slug)

        # Get the last 25 messages ordered by timestamp in descending order
        messages = Message.objects.filter(room=room).order_by('-timestamp')[:25]

        # Reverse the order of messages so that the oldest messages come first
        messages = messages[::-1]

        context = {'room': room, 'messages': messages}
        
        return render(request, 'app_room/room.html', context)
    
    except Room.DoesNotExist:
        msg.error(request, 'Room not found.')
        return render(request, 'app_room/room_not_found.html', status=404)

    except Exception as e:
        # Log the exception for debugging purposes
        print(f"An error occurred: {e}")
        msg.error(request, 'An error occurred.')
        return render(request, 'app_room/room_not_found.html', status=500)