from django.db import models
from apps.core.models import NameBaseModel


class Position(NameBaseModel):
    '''Job position model.'''

    class GradingScale(models.IntegerChoices):
        '''Job position grade.'''
        L1 = 1, '1'
        L2 = 2, '2'
        L3 = 3, '3'
        L4 = 4, '4'
        L5 = 5, '5'
        L6 = 6, '6'
        L7 = 7, '7'
        L8 = 8, '8'

    grade = models.PositiveSmallIntegerField(
        verbose_name='Грейд',
        choices=GradingScale.choices,
        default=GradingScale.L1,
    )
    unit = models.ForeignKey(
        'CompanyUnit',
        on_delete=models.SET_NULL,
        verbose_name='Подразделение',
        null=True,
    )

    class Meta(NameBaseModel.Meta):
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
