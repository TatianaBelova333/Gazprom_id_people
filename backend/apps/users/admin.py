from django.contrib import admin

from apps.users.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    '''Admin panel for the User model.'''
    list_display = (
        'id',
        'get_full_name',
        'email',
        'date_joined',
        'role',
    )
    list_filter = ('role',)
    ordering = ('last_name',)
    empty_value_display = "-пусто-"
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {
            "fields": (
                "first_name",
                "last_name",
                "middle_name",
                "phone_number",
            )
        }),
        ('Permissions', {
            'fields': ("role",)
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'first_name', 'last_name', 'password1', 'password2'
            ),
        }),
    )
