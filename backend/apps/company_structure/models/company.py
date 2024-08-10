from django.core.exceptions import ValidationError
from django.db import models


class Company(models.Model):
    '''Company singleton model. Only one Company instance may be created.'''
    name = models.CharField(
        max_length=100,
        verbose_name='Название',
    )

    description = models.TextField(
        verbose_name='Описание компании',
        blank=True,
    )

    director = models.OneToOneField(
        'staff.Employee',
        verbose_name='Владелец продукта',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='company',
    )

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компания'

    def __str__(self):
        return self.name

    def clean(self) -> None:
        '''Check if a Company instance already exists.'''
        if (not Company.objects.filter(pk=self.pk).exists()
                and Company.objects.exists()):
            raise ValidationError(
                'Компания может быть только одна.'
            )
        return super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
