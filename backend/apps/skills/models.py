from django.db import models


class Skill(models.Model):
    """
    Skill model for users' key skills.

    """
    name = models.CharField("Название", max_length=40, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "Ключевой навык"
        verbose_name_plural = "Ключевые навыки"

    def __str__(self):
        return self.name
