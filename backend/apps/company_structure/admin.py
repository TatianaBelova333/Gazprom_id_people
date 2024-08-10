from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from apps.company_structure.models import (
    Company,
    CompanyDepartment,
    CompanyOffice,
    CompanyTeam,
    CompanyUnit,
    Position
)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    '''Admin panel for the CompanyDepartment model.'''
    list_display = (
        'id',
        'name',
        'description',
        'director_link',
    )
    empty_value_display = "-пусто-"

    def director_link(self, obj):
        director = obj.director
        if director:
            url = reverse(
                'admin:staff_employee_changelist'
            ) + str(director.id)
            return format_html(f'<a href="{url}">{director}</a>')

    director_link.short_description = 'Руководитель компании'


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    '''Admin panel for the Job Position model.'''
    list_display = (
        'id',
        'name',
        'grade',
    )
    search_fields = ('name',)
    list_filter = ('grade',)


@admin.register(CompanyOffice)
class OfficeAdmin(admin.ModelAdmin):
    '''Admin panel for the CompanyOffice model.'''
    list_display = (
        'id',
        'name',
        'address',
        'company',
    )
    empty_value_display = "-пусто-"
    search_fields = ('name',)


@admin.register(CompanyUnit)
class UnitAdmin(admin.ModelAdmin):
    '''Admin panel for the CompanyUnit model.'''
    list_display = (
        'id',
        'name',
        'team_link',
    )
    empty_value_display = "-пусто-"
    search_fields = ('name',)
    list_filter = ('team',)

    def team_link(self, obj):
        team = obj.team
        if team:
            url = reverse(
                'admin:company_structure_companyteam_changelist'
            ) + str(team.id)
            return format_html(f'<a href="{url}">{team}</a>')

    team_link.short_description = 'Отдел'


@admin.register(CompanyTeam)
class TeamAdmin(admin.ModelAdmin):
    '''Admin panel for the CompanyTeam model.'''
    list_display = (
        'id',
        'name',
        'team_lead_link',
        'department',
    )
    empty_value_display = "-пусто-"
    search_fields = ('name',)
    list_filter = ('department',)

    def team_lead_link(self, obj):
        team_lead = obj.team_lead
        if team_lead:
            url = reverse(
                'admin:staff_employee_changelist'
            ) + str(team_lead.id)
            return format_html(f'<a href="{url}">{team_lead}</a>')

    team_lead_link.short_description = 'Руководитель отдела'


@admin.register(CompanyDepartment)
class DepartmentAdmin(admin.ModelAdmin):
    '''Admin panel for the CompanyDepartment model.'''
    list_display = (
        'id',
        'name',
        'head_link',
        'company',
    )
    empty_value_display = "-пусто-"
    search_fields = ('name',)

    def head_link(self, obj):
        head = obj.head
        if head:
            url = reverse(
                'admin:staff_employee_changelist'
            ) + str(head.id)
            return format_html(f'<a href="{url}">{head}</a>')

    head_link.short_description = 'Руководитель департамента'
