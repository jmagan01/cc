# Generated by Django 3.0.2 on 2020-04-18 01:58

import cwapi.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cwapi', '0055_auto_20200417_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='bidder',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='bidder_name',
        ),
        migrations.AddField(
            model_name='bid',
            name='bidder',
            field=models.CharField(default=1, max_length=25, verbose_name='Bidder name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='auction',
            name='ask_price',
            field=models.DecimalField(decimal_places=2, max_digits=12, validators=[cwapi.models.Auction.is_positive], verbose_name='Starting Price (£)'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='auction_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='cwapi.Auction'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bid_price',
            field=models.DecimalField(decimal_places=2, max_digits=12, validators=[cwapi.models.Bid.is_positive], verbose_name='Bid'),
        ),
    ]