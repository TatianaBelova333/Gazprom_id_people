from django.contrib import admin

from apps.staff.models import (
    Employee,
    EmployeeStatus,
    EmployeeTimeZone,
    SavedContact,
    Skill,
)
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(Employee)
class EmployeeAdmin(BaseUserAdmin):
    '''Admin panel for the Employee model.'''
    list_display = (
        'id',
        'get_full_name',
        'position',
        'unit',
        'email',
        'date_joined',
        'role',
        'status',
    )
    list_filter = (
        'role',
        'status',
        'unit',
        'unit__team',
        'unit__team__department',
    )
    ordering = ('last_name',)
    empty_value_display = "-пусто-"
    search_fields = ('last_name', 'skills__name', 'position__name')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Личная информация', {
            'fields': (
                'first_name',
                'last_name',
                'middle_name',
                'about_me',
                'phone_number',
                'timezone',
                'birthday',
                'image',
                'telegram',
            )
        }),
        ('Рабочая информация', {
            'fields': (
                'status',
                'skills',
                'office',
                'employment_type',
                'ms_teams',
                'position',
                'unit',
            )
        }),
        ('Доступы', {
            'fields': ("role",)
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'role', 'password1', 'password2'
            ),
        }),
    )
    list_select_related = (
        'status',
        'office',
        'unit',
        'position',
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    '''Admin panel for the Skill model.'''
    list_display = (
        'id',
        'name',
        'color',
    )
    search_fields = ('name',)


@admin.register(EmployeeStatus)
class EmployeeStatusAdmin(admin.ModelAdmin):
    '''Admin panel for the EmployeeStatus model.'''
    list_display = (
        'id',
        'name',
        'color',
    )
    search_fields = ('name',)


@admin.register(EmployeeTimeZone)
class TimeZoneAdmin(admin.ModelAdmin):
    '''Admin panel for the EmployeeTimeZone model.'''
    list_display = (
        'id',
        'name',
    )
    empty_value_display = "-пусто-"


@admin.register(SavedContact)
class SavedContactAdmin(admin.ModelAdmin):
    '''Admin panel for the EmployeeTimeZone model.'''
    list_display = (
        'id',
        'employee',
        'contact',
    )
    empty_value_display = "-пусто-"
