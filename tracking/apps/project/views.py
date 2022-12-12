# 
# import django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_list_or_404

# import models
from .models import Project
from apps.team.models import Team


# Create your views here.
@login_required
def projects(request):
    team = get_list_or_404(Team, pk=request.user.userprofile.active_team_id, status=Team.ACTIVE)
    projects = team.projects.all()

    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            project = Project.objects.create(team=team, title=title, created_by=request.user)

            return redirect('project:projects')

    return render(request, 'project/projects.html', {'team':team, 'projects':projects})
