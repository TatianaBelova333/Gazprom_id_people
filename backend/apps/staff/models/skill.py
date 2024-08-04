from apps.core.models import ColorBaseModel, NameBaseModel


class Skill(NameBaseModel, ColorBaseModel):
    '''Skill model for users' key skills.'''

    class Meta(NameBaseModel.Meta):
        verbose_name = 'Ключевой навык'
        verbose_name_plural = 'Ключевые навыки'
