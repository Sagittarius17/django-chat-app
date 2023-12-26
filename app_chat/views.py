from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import *

def index_view(request):
    return render(request, 'base.html')

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