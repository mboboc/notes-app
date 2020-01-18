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


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def display_notes(request):
    return request, 'display_notes.html'


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             auth_login(request, user)
#             return redirect('index.html')
#     else:
#         form = UserCreationForm()
#
#     context = {'form': form}
#     return render(request, 'signup.html', context)

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

# render = preia HTML
# redirect = te duce la pagina
# reverse
