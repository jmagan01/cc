# Generated by Django 2.2.12 on 2020-04-19 02:32

import cwapi.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cwapi', '0053_auto_20200417_1030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auction',
            options={},
        ),
        migrations.RenameField(
            model_name='auction',
            old_name='expiration_timedate',
            new_name='expiration_datetime',
        ),
        migrations.RenameField(
            model_name='auction',
            old_name='posted_timedate',
            new_name='posted_datetime',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='bidder_name',
        ),
        migrations.AddField(
            model_name='auction',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='auction',
            name='purchase_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=12, null=True, validators=[cwapi.models.Auction.is_positive], verbose_name='Purchase Price (£)'),
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
            model_name='auction',
            name='auction_status',
            field=models.CharField(default='Open', editable=False, max_length=25),
        ),
        migrations.AlterField(
            model_name='auction',
            name='auction_winner',
            field=models.CharField(default='To be confirmed', max_length=25),
        ),
        migrations.AlterField(
            model_name='auction',
            name='item_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Item Title'),
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
        migrations.AlterField(
            model_name='itemdetail',
            name='auction_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='item_details', to='cwapi.Auction'),
        ),
        migrations.AlterField(
            model_name='itemdetail',
            name='item_description',
            field=models.TextField(blank=True, max_length=500, verbose_name='Item Description'),
        ),
        migrations.AlterField(
            model_name='itemdetail',
            name='item_quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Quantity'),
        ),
        migrations.AlterUniqueTogether(
            name='auction',
            unique_together={('seller', 'id')},
        ),
    ]
