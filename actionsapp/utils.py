import datetime

from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

from actionsapp import models as actionsapp_models


def create_action(user, verb, target=None):
    # проверить, не было ли каких-либо аналогичных дейстивй
    # совершенных за последнюю минуту
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    simular_action = actionsapp_models.Action(user=user, verb=verb, created__gte=last_minute)

    if target:
        target_ct = ContentType.objects.get_for_model(target)
        simular_action = simular_action.objects.filter(target_ct=target_ct, targer_id=target.id)

    if not simular_action:
        action = actionsapp_models.Action(user=user, verb=verb, target=target)
        action.save()
        return True

    return False
