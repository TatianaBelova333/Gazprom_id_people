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
        validators=(MinLengthValidator(limit_value=2),),
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


class BusinessBaseModel(NameBaseModel):
    '''Abstract model for projects, services and components.'''

    description = models.TextField(
        verbose_name='Описание',
        max_length=3000,
        validators=(MinLengthValidator(limit_value=2),)
    )
    start_date = models.DateField(
        verbose_name='Дата начала',
        db_index=True,
        null=True,
        blank=True,
    )
    end_date = models.DateField(
        verbose_name='Дата окончания',
        db_index=True,
        null=True,
        blank=True,
    )
    status = models.ForeignKey(
        'projects.ProgressStatus',
        verbose_name='Статус работы',
        on_delete=models.PROTECT,
        related_name='%(class)ss',
        null=True,
    )
    tags = models.ManyToManyField(
        'projects.WorkTag',
        verbose_name='Теги',
        blank=True,
        related_name='%(class)ss',
    )
    team_members = models.ManyToManyField(
        'staff.Employee',
        verbose_name='Команда',
        related_name='%(class)ss',
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления',
    )
    is_archived = models.BooleanField(
        verbose_name='В архиве',
        default=False,
    )
    created_by = models.ForeignKey(
        'staff.Employee',
        verbose_name='Добавлен',
        related_name='%(class)ss_created',
        on_delete=models.SET_NULL,
        editable=False,
        blank=True,
        null=True,
    )
    updated_by = models.ForeignKey(
        'staff.Employee',
        verbose_name='Обновлен',
        related_name='%(class)ss_updated',
        on_delete=models.SET_NULL,
        editable=False,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('-start_date',)
        abstract = True
        constraints = [
            models.CheckConstraint(
                check=models.Q(end_date__gt=models.F('start_date')),
                name='%(class)s_end_date_greater_start_date',
                violation_error_message=(
                    'Дата окончания должны быть позднее даты начала.'
                ),
            )
        ]

    def __str__(self):
        return self.name
