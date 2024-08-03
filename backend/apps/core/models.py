from colorfield.fields import ColorField
from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower


class NameBaseModel(models.Model):
    '''Abstract model for models with the name field.'''
    name = models.CharField(
        max_length=50,
        verbose_name='Название',
    )

    class Meta:
        abstract = True
        ordering = ('name',)
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='%(class)s_unique_name',
                violation_error_message=(
                    'Данное название уже '
                    'существует.'
                ),
            )
        ]

    def __str__(self):
        return self.name


class ColorBaseModel(models.Model):
    '''Abstract model for models with the color field.'''
    color = ColorField(
        'Цвет тега',
        default='#D6E4FF',

    )

    class Meta:
        abstract = True
