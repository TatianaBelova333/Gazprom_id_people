from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from apps.projects.models import (
    Component,
    ProgressStatus,
    Project,
    Service,
    WorkTag,
)


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
        'description',
        'start_date',
        'end_date',
        'director_link',
        'created_at',
        'updated_at',
    )
    search_fields = ('name', 'description')
    ordering = ('start_date', 'end_date')

    def director_link(self, obj):
        director = obj.director
        if director:
            url = reverse(
                'admin:staff_employee_changelist'
            ) + str(director.id)
            return format_html(f'<a href="{url}">{director}</a>')

    director_link.short_description = 'Руководитель'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    '''Admin panel for the Service model.'''
    list_display = (
        'id',
        'name',
        'project',
        'description',
        'start_date',
        'end_date',
    )
    search_fields = ('name', 'description')
    ordering = ('start_date', 'end_date')


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    '''Admin panel for the Component model.'''
    list_display = (
        'id',
        'name',
        'service',
        'priority',
        'description',
        'start_date',
        'end_date',
    )
    search_fields = ('name', 'description')
    ordering = ('start_date', 'end_date')
    list_filter = ('priority',)
