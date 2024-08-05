from apps.core.models import ColorBaseModel, NameBaseModel


class WorkTag(NameBaseModel, ColorBaseModel):
    '''Work Tag model for projects, services and components.'''

    class Meta(NameBaseModel.Meta):
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
