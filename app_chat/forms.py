from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True, help_text='Enter your phone number.')

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'password1', 'password2')
