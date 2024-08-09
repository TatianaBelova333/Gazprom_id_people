from django.db import models

from apps.core.models import NameBaseModel


class CompanyDepartment(NameBaseModel):
    '''Company Department model.'''

    head = models.OneToOneField(
        'staff.Employee',
        verbose_name='Руководитель департмента',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='department',
     )
    product_owner = models.ForeignKey(
        'staff.Employee',
        verbose_name='Владелец продукта',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='departments',

    )

    class Meta(NameBaseModel.Meta):
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'
