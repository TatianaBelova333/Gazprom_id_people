from django.core.validators import MinLengthValidator
from django.db import models

from apps.core.models import BusinessBaseModel


class Project(BusinessBaseModel):
    '''Project model.'''

    director = models.ForeignKey(
        'staff.Employee',
        verbose_name='Руководитель проекта',
        on_delete=models.PROTECT,
    )

    class Meta(BusinessBaseModel.Meta):
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Service(BusinessBaseModel):
    '''Service model.'''

    project = models.ForeignKey(
        'Project',
        verbose_name='Проект',
        on_delete=models.PROTECT,
    )

    class Meta(BusinessBaseModel.Meta):
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'


class Component(BusinessBaseModel):
    '''Component model.'''

    class Priority(models.IntegerChoices):
        LOW = 1, '1/4'
        MEDIUM = 2, '2/4'
        HIGH = 3, '3/4'
        CRITICAL = 4, '4/4'

    service = models.ForeignKey(
        'Service',
        verbose_name='Сервис',
        on_delete=models.PROTECT,
    )
    release_type = models.CharField(
        verbose_name='Тип релиза',
        max_length=50,
        validators=[MinLengthValidator(limit_value=2)]
    )
    priority = models.PositiveSmallIntegerField(
        verbose_name='Приоритет',
        choices=Priority.choices,
        default=Priority.LOW,
    )

    class Meta(BusinessBaseModel.Meta):
        verbose_name = 'Компонент'
        verbose_name_plural = 'Компоненты'
