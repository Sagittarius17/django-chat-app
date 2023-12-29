from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib import messages as msg
from .models import *

@login_required
def rooms(request):
    rooms = Room.objects.all()
    
    return render(request, 'app_room/rooms.html', {'rooms': rooms})

@login_required
# def room(request, slug):
#     room = Room.objects.get(slug=slug)
#     messages = Message.objects.filter(room=room)[0:25]
    
#     return render(request, 'app_room/room.html', {'room': room}, {'messages': messages})

def room(request, slug):
    try:
        room = get_object_or_404(Room, slug=slug)
        messages = Message.objects.filter(room=room)[0:25]
        
        return render(request, 'app_room/room.html', {'room': room, 'messages': messages})
    
    except Room.DoesNotExist:
        msg.error(request, 'Room not found.')
        return render(request, 'app_room/room_not_found.html', status=404)

    except Exception as e:
        # Log the exception for debugging purposes
        print(f"An error occurred: {e}")
        msg.error(request, 'An error occurred.')
        return render(request, 'app_room/room_error.html', status=500)