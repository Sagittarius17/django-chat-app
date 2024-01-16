from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib import messages as msg
from .models import *

@login_required
def rooms(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    
    return render(request, 'app_room/rooms.html', context)


from itertools import groupby
from operator import attrgetter

@login_required
def room(request, slug):
    try:
        room = get_object_or_404(Room, slug=slug)

        # Get all messages for the room ordered by timestamp
        messages = Message.objects.filter(room=room).order_by('timestamp')

        # Group messages by date
        grouped_messages = []
        for date, group in groupby(messages, key=attrgetter('timestamp.date')):
            date_messages = list(group)
            grouped_messages.append({
                'date': date,
                'messages': date_messages,
            })

        context = {'room': room, 'grouped_messages': grouped_messages}
        
        return render(request, 'app_room/room.html', context)
    
    except Room.DoesNotExist:
        msg.error(request, 'Room not found.')
        return render(request, 'app_room/room_not_found.html', status=404)

    except Exception as e:
        # Log the exception for debugging purposes
        print(f"An error occurred: {e}")
        msg.error(request, 'An error occurred.')
        return render(request, 'app_room/room_not_found.html', status=500)
