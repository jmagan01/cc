# Generated by Django 3.0.2 on 2020-04-12 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cwapi', '0010_auto_20200412_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='auction_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False, unique=True, verbose_name='Auction identifier'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='auction',
            name='item_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='cwapi.Item'),
        ),
    ]
