# Generated by Django 3.0.2 on 2020-04-18 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cwapi', '0056_auto_20200418_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='owner',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]