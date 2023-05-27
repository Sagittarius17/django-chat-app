from django.shortcuts import render, redirect

# Create your views here.
# videoshare/app/views.py

def main_layout(request):
    return render(request, 'main/index.html')

from .models import Room

def video_chat_room(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        if room_name:
            room = Room.objects.create(name=room_name)
            # You can perform additional operations with the room object if needed
            return render(request, 'main/room.html', {'room': room})
    return render(request, 'main/room.html')


