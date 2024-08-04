from apps.core.models import ColorBaseModel, NameBaseModel


class EmployeeStatus(NameBaseModel, ColorBaseModel):
    '''Employee's work status model.'''

    class Meta(NameBaseModel.Meta):
        verbose_name = 'Рабочий статус'
        verbose_name_plural = 'Рабочие статусы'
