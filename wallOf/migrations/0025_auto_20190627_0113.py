# Generated by Django 2.2.1 on 2019-06-27 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallOf', '0024_auto_20190627_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelposts',
            name='up_vote',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
