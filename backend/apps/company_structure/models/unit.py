from django.db import models
from apps.core.models import NameBaseModel


class CompanyUnit(NameBaseModel):
    '''Company Unit model (Подразделения).'''

    team = models.ForeignKey(
        'CompanyTeam',
        verbose_name='Отдел',
        related_name='units',
        on_delete=models.PROTECT,
    )

    class Meta(NameBaseModel.Meta):
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
