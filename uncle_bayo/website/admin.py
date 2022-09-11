from django.contrib import admin
from .models import Work, Team

# Register your models here.


class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'summary', 'image', 'areas',)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'image',)


admin.site.register(Work, WorkAdmin)
admin.site.register(Team, TeamAdmin)
