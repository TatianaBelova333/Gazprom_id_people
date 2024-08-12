from pytils.translit import slugify


def images_directory_path(instance, filename) -> str:
    '''Define structure for storing models' images.'''
    return '{0}/{1}/{2}'.format(
        instance.__class__.__name__,
        slugify(instance),
        filename
    )


def delete_related_model_image(sender, instance, **kwargs):
    '''Delete model's image when deleting a model instance.'''
    if instance.image:
        storage, path = instance.image.storage, instance.image.path
        storage.delete(path)


def delete_old_model_image_edit(sender, instance, **kwargs):
    '''Delete the model's old image when adding a new image.'''
    if instance and instance.id:
        old_instance = sender.objects.filter(pk=instance.id).first()
        if old_instance:
            if old_instance.image != instance.image:
                old_instance.image.delete(save=False)
