# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('<int:team_id>/scores/', views.team_scores, name='team_scores'),
]



