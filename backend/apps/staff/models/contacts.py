from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import F, Q

Employee = get_user_model()


class SavedContact(models.Model):
    '''Model for adding users to employees' contacts.'''
    employee = models.ForeignKey(
        Employee,
        related_name='contacts',
        on_delete=models.CASCADE,
        verbose_name='Сотрудник',
    )
    contact = models.ForeignKey(
        Employee,
        related_name='added_by',
        on_delete=models.CASCADE,
        verbose_name='Сохраненный контакт',
    )

    class Meta:
        unique_together = ('employee', 'contact')
        verbose_name = 'Сохранненый контакт'
        verbose_name_plural = 'Сохранненые контакты'
        constraints = [
            models.UniqueConstraint(
                fields=('employee', 'contact'),
                name='unique_contact',
                violation_error_message=(
                    'Контакт уже добавлен.'
                )
            ),
            models.CheckConstraint(
                check=~Q(employee=F('contact')),
                name='employee_manager_constraint',
                violation_error_message=(
                    'Нельзя добавлять в контакты самого себя.'
                ),
            )
        ]

    def __str__(self):
        return f'{self.contact}'
