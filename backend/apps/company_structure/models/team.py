from django.db import models

from apps.core.models import NameBaseModel


class CompanyTeam(NameBaseModel):
    '''Company Team model (Отделы).'''

    team_lead = models.OneToOneField(
        'staff.Employee',
        verbose_name='Руководитель отдела',
        on_delete=models.PROTECT,
        related_name='team',
        null=True,
        blank=True,
    )
    department = models.ForeignKey(
        'company_structure.CompanyDepartment',
        verbose_name='Департамент',
        on_delete=models.PROTECT,
        related_name='teams',
        null=True,
        blank=True,
    )

    class Meta(NameBaseModel.Meta):
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
