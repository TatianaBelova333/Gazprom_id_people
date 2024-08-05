from django.contrib import admin

from apps.business.models import ProgressStatus, Project, WorkTag


@admin.register(ProgressStatus)
class ProgressStatusAdmin(admin.ModelAdmin):
    '''Admin panel for the ProgressStatus model.'''
    list_display = (
        'id',
        'name',
        'color',
    )
    search_fields = ('name',)


@admin.register(WorkTag)
class TagAdmin(admin.ModelAdmin):
    '''Admin panel for the WorkTag model.'''
    list_display = (
        'id',
        'name',
        'color',
    )
    search_fields = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    '''Admin panel for the Project model.'''
    list_display = (
        'id',
        'name',
        'director',
        'description',
        'date_start',
        'date_end',
    )
    search_fields = ('name', 'description')
