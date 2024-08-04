from django.contrib import admin

from apps.company_structure.models import (
    CompanyDepartment,
    CompanyOffice,
    CompanyTeam,
    CompanyUnit,
    Position
)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    '''Admin panel for the Job Position model.'''
    list_display = (
        'id',
        'name',
        'grade',
        'unit'
    )
    search_fields = ('name',)
    list_filter = ('grade', 'unit')


@admin.register(CompanyOffice)
class OfficeAdmin(admin.ModelAdmin):
    '''Admin panel for the CompanyOffice model.'''
    list_display = (
        'id',
        'name',
        'address',
    )
    empty_value_display = "-пусто-"
    search_fields = ('name',)


@admin.register(CompanyUnit)
class UnitAdmin(admin.ModelAdmin):
    '''Admin panel for the CompanyUnit model.'''
    list_display = (
        'id',
        'name',
        'team',
    )
    empty_value_display = "-пусто-"
    search_fields = ('name',)
    list_filter = ('team',)


@admin.register(CompanyTeam)
class TeamAdmin(admin.ModelAdmin):
    '''Admin panel for the CompanyTeam model.'''
    list_display = (
        'id',
        'name',
        'team_lead',
        'department',
    )
    empty_value_display = "-пусто-"
    search_fields = ('name',)
    list_filter = ('department',)


@admin.register(CompanyDepartment)
class DepartmentAdmin(admin.ModelAdmin):
    '''Admin panel for the CompanyDepartment model.'''
    list_display = (
        'id',
        'name',
        'head'
    )
    empty_value_display = "-пусто-"
    search_fields = ('name',)
