# Generated by Django 4.2.1 on 2023-07-24 17:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RecipeO',
            new_name='Recipe',
        ),
    ]
