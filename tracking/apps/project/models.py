# import django 
from django.contrib.auth.models import User
from django.db import models


# import models 
from apps.team.models import Team


# Create your models here.
class Project(models.Model):
    team = models.ForeignKey(Team, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    created_by = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
    
    def registered_time(self):
        return sum(entry.minutes for entry in self.entries.all())
    
    def num_tasks_todo(self):
        return self.task.filter(status=Task.TODO).count()



class Task(models.Model):
    # 
    # status updates

    TODO = 'todo'
    DONE = 'done'
    ARCHIVED = 'archived'

    CHOICES_STATUS = (
        (TODO, 'Todo'),
        (DONE, 'Done'),
        (ARCHIVED, 'Archived')
    )

    team = models.ForeignKey(Team, related_name='tasks', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=TODO)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def registered_time(self):
        return sum(entry.minutes for entry in self.entries.all())


class Entry(models.Model):
    team = models.ForeignKey(Team, related_name='entries', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='entries', on_delete=models.CASCADE, blank=True, null=True)
    task = models.ForeignKey(Task, related_name='entries', on_delete=models.CASCADE, blank=True, null=True)
    minutes = models.IntegerField(default=0)
    is_tracked = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE)
    created_at = models.DateTimeField()


    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        if self.task:
            return '%s - %s' % (self.task.title, self.created_at)
        
        return '%s' % self.created_at