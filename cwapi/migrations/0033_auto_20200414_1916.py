# Generated by Django 3.0.2 on 2020-04-14 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cwapi', '0032_auto_20200414_0245'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItemDetail',
            new_name='Item',
        ),
    ]