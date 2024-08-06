from apps.core.models import NameBaseModel


class EmployeeTimeZone(NameBaseModel):
    '''Timezone model for the employee's location.'''

    class Meta(NameBaseModel.Meta):
        ordering = ('id',)
        verbose_name = 'Часовой пояс'
        verbose_name_plural = 'Часовые пояса'
