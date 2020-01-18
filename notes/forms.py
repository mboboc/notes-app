from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, Select

from notes.models import Note


class UserCreationForm(forms.ModelForm):
    # avem nevoie de asta ca sa modific formularul
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'First Name', 'class': 'navbar-end'}),
            'last_name': TextInput(attrs={'placeholder': 'Last Name', 'class': 'navbar-end'}),
            'email': TextInput(attrs={'placeholder': 'Email', 'class': 'navbar-end'}),
        }

class UserNotesForm(forms.ModelForm):
    # avem nevoie de asta ca sa modific formularul
    class Meta:
        model = Note
        fields = ['user', 'title', 'note']

        widgets = {
            'user': Select(attrs={'placeholder': 'User', 'class': 'navbar-end'}),
            'title': TextInput(attrs={'placeholder': 'Title', 'class': 'navbar-end'}),
            'email': TextInput(attrs={'placeholder': 'Email', 'class': 'navbar-end'}),
        }
