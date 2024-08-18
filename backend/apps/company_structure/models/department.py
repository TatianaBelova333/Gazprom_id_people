from django.db import models

from apps.core.models import NameBaseModel


class CompanyDepartment(NameBaseModel):
    '''Company Department model (Департаменты).'''

    head = models.OneToOneField(
        'staff.Employee',
        verbose_name='Руководитель департмента',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='department',
     )
    company = models.ForeignKey(
        'Company',
        verbose_name='Компания',
        on_delete=models.PROTECT,
        related_name='departments',
    )

    class Meta(NameBaseModel.Meta):
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'
