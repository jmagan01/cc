# Generated by Django 3.0.2 on 2020-04-14 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cwapi', '0033_auto_20200414_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='starting_price',
        ),
        migrations.AddField(
            model_name='auction',
            name='ask_price',
            field=models.PositiveIntegerField(default=10, verbose_name='Minimun Price'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Quantity'),
        ),
    ]