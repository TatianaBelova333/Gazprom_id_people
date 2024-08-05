from colorfield.fields import ColorField
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower


class NameBaseModel(models.Model):
    '''Abstract model for models with the name field.'''
    name = models.CharField(
        max_length=50,
        verbose_name='Название',
        validators=[MinLengthValidator(limit_value=2)]
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


class BusinessBaseModel(models.Model):
    '''Abstract model for projects, services and tags.'''
    description = models.TextField(
        verbose_name='Описание',
        max_length=3000,
        blank=True,
    )
    date_start = models.DateField(
        verbose_name='Дата начала',
        blank=True,
        null=True,
    )
    date_end = models.DateField(
        verbose_name='Дата окончания',
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True
