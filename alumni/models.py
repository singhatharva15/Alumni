from weakref import proxy
from django.db import models

from accounts.models import User


class Career(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    s_date = models.DateField(auto_now=False, auto_now_add=False)
    e_date = models.DateField(auto_now=False, auto_now_add=False)
    present = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email


class Events(models.Model):
    event_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    Remark = models.TextField()

    def __str__(self):
        return self.event_name

    class Meta:
        verbose_name_plural = "Events"


class Opportunities(models.Model):
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    criteria = models.CharField(max_length=100)
    remark = models.TextField()

    class Meta:
        verbose_name_plural = "Opportunities"


# class UserProxy(User):
#     class Meta:
#         proxy = True
        # class UserCert(models.Model):
        #     # certificate related fileds
        #     user = models.ForeignKey(User, on_delete=models.CASCADE)
        #     display_name = models.CharField(max_length=254, null=True, blank=True)
        #     show_cert = models.BooleanField(default=False)

        #     def __str__(self) -> str:
        #         return self.user.email
