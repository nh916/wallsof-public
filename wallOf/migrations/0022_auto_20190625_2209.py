# Generated by Django 2.2.1 on 2019-06-26 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallOf', '0021_auto_20190625_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelposts',
            name='title',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
