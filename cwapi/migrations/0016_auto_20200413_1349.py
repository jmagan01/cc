# Generated by Django 3.0.2 on 2020-04-13 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cwapi', '0015_auto_20200413_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='time_left',
            field=models.DateTimeField(blank=True, verbose_name='Days to complete'),
        ),
    ]
