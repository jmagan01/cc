# Generated by Django 3.0.2 on 2020-04-11 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cwapi', '0008_auto_20200411_0037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('auction_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('time_left', models.DurationField()),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cwapi.Item')),
            ],
        ),
    ]
