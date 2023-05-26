from django.shortcuts import render, redirect

# Create your views here.
# videoshare/app/views.py

def video_chat_room(request):
    return render(request, 'main/room.html')

