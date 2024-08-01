from apps.core.models import ColorBaseModel, NameBaseModel


class EmployeeStatus(NameBaseModel, ColorBaseModel):
    '''Employee's personal status model.'''

    class Meta(NameBaseModel.Meta):
        verbose_name = 'Личный статус'
        verbose_name_plural = 'Личные статусы'
