# Generated by Django 2.2.1 on 2019-05-26 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallOf', '0003_auto_20190525_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelposts',
            name='vote',
            field=models.CharField(choices=[('vote_here', 'vote_here'), ('down', 'down')], default=0, max_length=2, null=True),
        ),
    ]
