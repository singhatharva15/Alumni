# Generated by Django 4.0.4 on 2022-09-29 03:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alumni', '0006_eventattendees_oppaplications_delete_userproxy'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OppAplications',
            new_name='Applications',
        ),
        migrations.AlterModelOptions(
            name='eventattendees',
            options={},
        ),
        migrations.AlterModelOptions(
            name='opportunities',
            options={},
        ),
    ]