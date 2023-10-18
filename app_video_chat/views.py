from django.shortcuts import render

# Create your views here.

def base_view(request):
    return render(request, 'app_video_chat/base.html')
