# Generated by Django 3.0.2 on 2020-04-13 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cwapi', '0020_auto_20200413_1759'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auction',
            options={'ordering': ['auction_status']},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-expiration_timedate']},
        ),
        migrations.RenameField(
            model_name='item',
            old_name='date_posted',
            new_name='posted_timedate',
        ),
    ]
