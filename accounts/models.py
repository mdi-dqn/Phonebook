from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
