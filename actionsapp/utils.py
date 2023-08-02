from actionsapp import models as actionsapp_models


def create_action(user, verb, target=None):
    action = actionsapp_models.Action(user=user, verb=verb, target=target)
    action.save()
