# Generated by Django 3.2 on 2021-05-18 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
