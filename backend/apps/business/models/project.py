from django.db import models

from apps.core.models import BusinessBaseModel, NameBaseModel


class Project(NameBaseModel, BusinessBaseModel):
    '''Project model.'''

    director = models.ForeignKey(
        'staff.Employee',
        verbose_name='Руководитель проекта',
        on_delete=models.PROTECT,
    )
    status = models.ForeignKey(
        'ProgressStatus',
        verbose_name='Статус работы',
        on_delete=models.SET_NULL,
        null=True,
    )
    tags = models.ManyToManyField(
        'WorkTag',
        verbose_name='Теги проекта',
        blank=True,
        related_name='projects',
    )

    class Meta(NameBaseModel.Meta):
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
