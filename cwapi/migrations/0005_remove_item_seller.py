# Generated by Django 3.0.2 on 2020-04-05 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cwapi', '0004_auto_20200405_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='seller',
        ),
    ]
