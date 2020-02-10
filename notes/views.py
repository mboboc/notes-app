from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from notes.forms import UserNotesForm
from notes.models import Note


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('notes:home')
        else:
            return render(request, 'registration/login.html', {'error': 'username or password incorrect.'})
    else:
        return render(request, 'registration/login.html')


def index(request):
    return render(request, 'index.html')


def edit_note(request):
    context={

    }
    return render(request, 'display_notes.html', context)

@login_required
def home(request):
    current_user = request.user
    context = {'current_user': current_user}
    return render(request, 'home.html', context)


@login_required
def display_notes(request):
    current_user = request.user.username
    current_user_id = User.objects.get(username=current_user)
    user_notes = Note.objects.filter(user_id=current_user_id)
    context = {
        'user_notes': user_notes,
        'current_user': current_user,
    }
    return render(request, 'display_notes.html', context)


class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'signup.html'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect('login')


class CreateNoteView(CreateView):
    model = Note
    form_class = UserNotesForm
    template_name = 'create_note.html'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect('notes:home')
