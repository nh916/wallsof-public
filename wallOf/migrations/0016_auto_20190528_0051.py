# Generated by Django 2.2.1 on 2019-05-28 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallOf', '0015_auto_20190527_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelposts',
            name='down_vote',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='modelposts',
            name='up_vote',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
