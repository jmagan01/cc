# Generated by Django 3.0.2 on 2020-04-13 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cwapi', '0027_remove_auction_auction_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Active'), (1, 'Closed')], default=0),
        ),
    ]