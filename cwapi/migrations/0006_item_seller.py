# Generated by Django 3.0.2 on 2020-04-05 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cwapi', '0005_remove_item_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='seller',
            field=models.CharField(default='Admin', max_length=25),
            preserve_default=False,
        ),
    ]