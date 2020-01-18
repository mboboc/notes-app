from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField('Title', max_length=100, blank=True, null=True)
    date=models.DateTimeField('Date', blank=100, null=True)
    note=models.CharField('Note', max_length=1000, blank=True, null=True)

