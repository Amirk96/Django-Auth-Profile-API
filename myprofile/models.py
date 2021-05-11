from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class MyProfileModel(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        )    
    mobile = models.CharField(max_length=100, unique=True)
    profile_picture = models.ImageField(upload_to='thumbpath', blank=True)
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


