# Generated by Django 4.0.4 on 2022-09-03 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'verbose_name_plural': 'Events'},
        ),
        migrations.AlterModelOptions(
            name='opportunities',
            options={'verbose_name_plural': 'Opportunities'},
        ),
    ]