from django.contrib import admin

# Register your models here.

from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_filter = ['created']
    list_display = ['name', "created"]
    