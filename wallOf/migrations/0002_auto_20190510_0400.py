# Generated by Django 2.2.1 on 2019-05-10 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallOf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelposts',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='modelposts',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
