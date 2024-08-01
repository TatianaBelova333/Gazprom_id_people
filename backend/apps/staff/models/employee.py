from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models
from django.db.models import F, Q
from phonenumber_field.modelfields import PhoneNumberField

from apps.staff.managers import CustomUserManager, UserRoles


class Employee(
    AbstractBaseUser,
    PermissionsMixin,
):
    '''
    Custom User model for employees.
    Email and password required for authorization.
    '''
    first_name = models.CharField('Имя', max_length=50, blank=True)
    last_name = models.CharField('Фамилия', max_length=50, blank=True)
    middle_name = models.CharField('Отчество', max_length=50, blank=True)
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата регистрации',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления',
    )
    is_active = models.BooleanField(default=True)
    email = models.EmailField('Email адрес', unique=True)
    phone_number = PhoneNumberField(
        'Номер телефона',
        blank=True,
        null=True,
        unique=True,
    )
    birthday = models.DateField(
        'День рождения',
        blank=True,
        null=True,
    )
    about_me = models.TextField(
        'О себе',
        blank=True,
    )
    role = models.CharField(
        'Тип учетной записи',
        max_length=5,
        choices=UserRoles.choices,
        default=UserRoles.USER,
    )
    status = models.ForeignKey(
        'EmployeeStatus',
        verbose_name='Статус',
        on_delete=models.SET_NULL,
        null=True,
    )
    skills = models.ManyToManyField(
        'Skill',
        verbose_name='Навыки',
        related_name='employees',
        blank=True,
    )
    manager = models.ForeignKey(
        'self',
        verbose_name='Руководитель',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        constraints = [
            models.CheckConstraint(
                check=~Q(pk=F('manager')),
                name='employee_manager_constraint',
            )
        ]

    def __str__(self):
        full_name = self.get_full_name()
        return full_name or self.email

    def get_full_name(self):
        '''Returns employee's full name.'''
        full_name = " ".join(
            (self.last_name, self.first_name, self.middle_name)
        )
        return full_name.strip().title()

    get_full_name.short_description = "ФИО"
