from django.db import models

from accounts.models import User

class Career(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    s_date = models.DateField(auto_now=False, auto_now_add=False)
    e_date = models.DateField(auto_now=False, auto_now_add=False)
    present = models.BooleanField(default=False)

class Events(models.Model):
    event_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    Remark = models.TextField()


class Opportunities(models.Model):
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    criteria = models.CharField(max_length=100)
    remark = models.TextField()