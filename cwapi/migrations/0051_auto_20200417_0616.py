# Generated by Django 3.0.2 on 2020-04-17 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cwapi', '0050_auto_20200416_1919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='bidder',
            new_name='bidder_name',
        ),
        migrations.AlterField(
            model_name='auction',
            name='auction_winner',
            field=models.CharField(default=None, editable=False, max_length=25),
        ),
    ]
