from django.contrib import admin

# Register your models here.

from .models import Activities

@admin.register(Activities)
class ActivitiesAdmim(admin.ModelAdmin):
    list_filter = ['team', 'created']