# Generated by Django 2.2.1 on 2019-06-27 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallOf', '0029_auto_20190627_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeladvice',
            name='up_vote',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='modelsecretes',
            name='up_vote',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
