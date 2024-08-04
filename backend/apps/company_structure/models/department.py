from django.db import models

from apps.core.models import NameBaseModel


class CompanyDepartment(NameBaseModel):
    '''Company Department model.'''

    head = models.OneToOneField(
        'staff.Employee',
        verbose_name='Руководитель департмента',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='department',
     )

    class Meta(NameBaseModel.Meta):
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'
