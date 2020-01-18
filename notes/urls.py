from django.urls import path
from notes import views

app_name = 'notes'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name="login"),
    path('home/', views.home, name="home"),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('create_note/', views.CreateNoteView.as_view(), name="create_note")
    ]