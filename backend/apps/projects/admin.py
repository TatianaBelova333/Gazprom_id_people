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
        'created_by',
        'updated_by',
    )
    search_fields = ('name', 'description')
    ordering = ('start_date', 'end_date')
    list_filter = ('is_archived', 'status')
    list_select_related = (
        'status',
        'director__position',
        'created_by',
        'updated_by',
    )

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
        'status',
        'description',
        'start_date',
        'end_date',
        'created_by',
        'updated_by',
    )
    search_fields = ('name', 'description')
    ordering = ('start_date', 'end_date')
    list_filter = ('is_archived', 'status')
    list_select_related = (
        'status',
        'project',
        'created_by',
        'updated_by',
    )


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    '''Admin panel for the Component model.'''
    list_display = (
        'id',
        'name',
        'service',
        'status',
        'priority',
        'description',
        'start_date',
        'end_date',
        'created_by',
        'updated_by',
    )
    search_fields = ('name', 'description')
    ordering = ('start_date', 'end_date')
    list_filter = ('priority', 'is_archived', 'status')
    list_select_related = (
        'status',
        'service',
        'created_by',
        'updated_by',
    )
