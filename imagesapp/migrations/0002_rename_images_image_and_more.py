# Generated by Django 4.1.9 on 2023-07-16 23:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("imagesapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Images",
            new_name="Image",
        ),
        migrations.RenameIndex(
            model_name="image",
            new_name="imagesapp_i_created_3285c8_idx",
            old_name="imagesapp_i_created_ea0906_idx",
        ),
    ]
