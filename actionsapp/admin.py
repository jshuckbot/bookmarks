from django.contrib import admin

from actionsapp import models as actionapp_models


@admin.register(actionapp_models.Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ["user", "verb", "target", "created"]
    list_filter = ["created"]
    search_fields = ["verb"]
