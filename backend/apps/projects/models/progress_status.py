from apps.core.models import ColorBaseModel, NameBaseModel


class ProgressStatus(NameBaseModel, ColorBaseModel):
    '''Progress Status model for projects, services and components.'''

    class Meta(NameBaseModel.Meta):
        verbose_name = 'Статус работы'
        verbose_name_plural = 'Статусы работы'
