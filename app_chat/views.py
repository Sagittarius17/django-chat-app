from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import *

def welcome(request):
    return render(request, 'app_chat/welcome.html')

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            
            return redirect('welcome')
    else:
        form = SignUpForm()
    
    return render(request, 'app_chat/signup.html', {'form': form})

