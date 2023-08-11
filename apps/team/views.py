from django.shortcuts import render

# Create your views here.
from .models import Team

def team_scores(request, team_id):
    team = Team.objects.get(pk=team_id)
    activities = team_id.activities.all() 

    return render(request, 
                  'team/detail.hml',
                  {
                      'team': team,
                      'activities': activities,
                  })
