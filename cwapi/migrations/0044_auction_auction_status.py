# Generated by Django 3.0.2 on 2020-04-15 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cwapi', '0043_remove_auction_auction_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='auction_status',
            field=models.CharField(default='Active', max_length=25, verbose_name='Auction status'),
        ),
    ]
