from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.projects.models import Project


@receiver(post_save, sender=Project)
def create_added_to_project_notification(sender, instance, updated):
    pass
