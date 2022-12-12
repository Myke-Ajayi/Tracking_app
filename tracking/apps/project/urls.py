# import django
from django.urls import path

# import views
from .views import projects

# create url pattern
app_name = 'project'

urlpatterns = [
    path('', projects, name='projects'),
]


