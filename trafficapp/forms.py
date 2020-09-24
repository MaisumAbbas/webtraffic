from django import forms
from django.contrib.auth.models import User
from trafficapp.models import TrafficGenerateRequest

class UserForm(forms.ModelForm):
    password = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

class TrafficRequestForm(forms.ModelForm):
    class Meta:
        model = TrafficGenerateRequest
        fields = ('name', 'email', 'company', 'url', 'minimum', 'maximum', 'requests', 'stay')