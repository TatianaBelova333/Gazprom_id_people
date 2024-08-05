from django.db import models


class CompanyOffice(models.Model):
    '''Company office model.'''
    name = models.CharField(
        verbose_name='Название офиса',
        max_length=100,
        blank=True,
    )
    address = models.TextField(
        verbose_name='Адрес',
        unique=True,
    )

    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы'

    def __str__(self):
        if self.name:
            return f'{self.name}, {self.address}'
        return self.address
