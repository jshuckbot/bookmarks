from django.contrib import admin

from accountapp.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "date_of_birth", "photo"]
    raw_id_fields = ["user"]
