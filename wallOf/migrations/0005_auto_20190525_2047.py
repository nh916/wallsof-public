# Generated by Django 2.2.1 on 2019-05-26 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallOf', '0004_auto_20190525_2046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelposts',
            old_name='emotion',
            new_name='rant',
        ),
    ]
