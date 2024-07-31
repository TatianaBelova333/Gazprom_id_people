from django.db import models


class NameBaseModel(models.Model):
    '''Abstract model for models with the name field.'''
    title = models.CharField(
        max_length=50,
        verbose_name='Название',
    )

    class Meta:
        abstract = True
