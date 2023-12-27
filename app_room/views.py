from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import *

@login_required
def rooms(request):
    rooms = Room.objects.all()
    
    return render(request, 'app_room/rooms.html', {'rooms': rooms})