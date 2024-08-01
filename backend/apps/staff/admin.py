from django.contrib import admin

from apps.staff.models import Employee, EmployeeStatus, Skill
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(Employee)
class EmployeeAdmin(BaseUserAdmin):
    '''Admin panel for the Employee model.'''
    list_display = (
        'id',
        'get_full_name',
        'email',
        'date_joined',
        'manager',
        'role',
        'status',
    )
    list_filter = ('role', 'status')
    ordering = ('last_name',)
    empty_value_display = "-пусто-"
    search_fields = ('last_name', 'skills__name')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Личная информация', {
            'fields': (
                'first_name',
                'last_name',
                'middle_name',
                'about_me',
                'phone_number',
                'status',
                'skills',
                'manager',
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
                'email', 'password1', 'password2'
            ),
        }),
    )
    list_select_related = ('status',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    '''Admin panel for the Skill model.'''
    list_display = (
        'id',
        'name',
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
