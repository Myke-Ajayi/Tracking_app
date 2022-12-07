
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# 
class Team(models.Model):
    # 
    # 

    ACTIVE = 'active'
    DELETED = 'deleted'

    CHOICES_STATUS = (
    (ACTIVE, 'Active'),
    (DELETED, 'Deleted')
    )
    # Fields

    title = models.CharField(max_length=225)
    members = models.ManyToManyField(User, related_name='teams')
    created_by = models.ForeignKey(User, related_name='created_teams', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    