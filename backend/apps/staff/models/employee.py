from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.core.validators import URLValidator
from phonenumber_field.modelfields import PhoneNumberField

from apps.core.utils import images_directory_path
from apps.staff.managers import CustomUserManager, UserRoles


class Employee(
    AbstractBaseUser,
    PermissionsMixin,
):
    '''
    Custom User model for employees.
    Email and password required for authorization.
    '''
    class EmployementTypes(models.IntegerChoices):
        staff = 0, 'Штат'
        outsource = 1, 'Аутсорс'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    role = models.CharField(
        'Тип учетной записи',
        max_length=5,
        choices=UserRoles.choices,
        default=UserRoles.USER,
    )
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
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to=images_directory_path,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True)
    email = models.EmailField('Email адрес', unique=True)
    phone_number = PhoneNumberField(
        'Номер телефона',
        blank=True,
        null=True,
        unique=True,
        region="RU",
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
    timezone = models.ForeignKey(
        'EmployeeTimeZone',
        verbose_name='Часовой пояс',
        on_delete=models.SET_NULL,
        null=True,
    )
    telegram = models.URLField(
        verbose_name='Telegram-аккаунт',
        null=True,
        blank=True,
        unique=True,
        validators=(URLValidator(
            regex=r'^https:\/\/t\.me\/\w{5,32}$',
            message='Ссылка на телеграм аккуант должны быть '
                    'в следующем формате: https://t.me/<tg-username>'
        ),),
        help_text=('Введите телеграм аккуант в следующем формате: '
                   'https://t.me/<tg-username>')
    )
    ms_teams = models.EmailField(
        verbose_name='MS Teams',
        unique=True,
        null=True,
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
    office = models.ForeignKey(
        'company_structure.CompanyOffice',
        verbose_name='Офис',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    position = models.ForeignKey(
        'company_structure.Position',
        verbose_name='Должность',
        on_delete=models.PROTECT,
        null=True,
    )
    unit = models.ForeignKey(
        'company_structure.CompanyUnit',
        verbose_name='Подразделение',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='employees',
    )
    employment_type = models.PositiveSmallIntegerField(
        verbose_name='Форма трудоустройства',
        choices=EmployementTypes.choices,
        default=EmployementTypes.staff,
    )

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ('-position__grade', 'last_name')

    def __str__(self):
        short_name = self.get_short_name()
        user_indenity = short_name or self.email
        position = self.position or '-'
        return f'{user_indenity}, {position}'

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

    def get_full_name(self):
        '''Returns employee's full name.'''
        full_name = " ".join(
            (self.last_name, self.first_name, self.middle_name)
        )
        return full_name.strip().title()

    def get_short_name(self):
        '''Returns employee's short name.'''
        short_name = []
        if self.last_name:
            short_name.append(self.last_name)
        if self.first_name:
            short_name.append(f'{self.first_name[0]}.')
        if self.middle_name:
            short_name.append(f'{self.middle_name[0]}.')

        return ' '.join(short_name).title()

    get_full_name.short_description = "ФИО"
