from django.contrib.auth import get_user_model
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from apps.core.utils import (
    delete_old_model_image_edit,
    delete_related_model_image,

)

Employee = get_user_model()

receiver(post_delete, sender=Employee)(delete_related_model_image)
receiver(pre_save, sender=Employee)(delete_old_model_image_edit)
