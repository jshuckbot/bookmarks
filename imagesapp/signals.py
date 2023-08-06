from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from imagesapp import models as imagesapp_models


@receiver(m2m_changed, sender=imagesapp_models.Image.user_like.through)
def users_like_changed(sender, instance, **kwargs):
    instance.total_likes = instance.user_like.count()
    instance.save()
