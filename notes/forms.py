from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, Select

from notes.models import Note


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']


class UserNotesForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['user', 'title', 'note']
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Note title', 'class': 'form-control'}),
            'note': TextInput(attrs={'placeholder': '', 'Note': 'form-control'}),
        }


