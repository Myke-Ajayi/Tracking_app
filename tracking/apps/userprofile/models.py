

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# Models

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofie', on_delete=models.CASCADE)
    active_team_id = models.IntegerField(default=0)