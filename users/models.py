from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=300)
    birthday = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} Profile'

