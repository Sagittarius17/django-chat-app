from django import forms
from .models import Video, Audio

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'file']

class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['title', 'file']
