# Generated by Django 2.2.1 on 2019-11-11 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallOf', '0034_modelposts_red_flag'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelJoy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('joy', models.TextField(max_length=240)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('only_date', models.DateField(auto_now_add=True)),
                ('up_vote', models.IntegerField(blank=True, default=0)),
                ('down_vote', models.IntegerField(blank=True, default=0)),
                ('RED_FLAG', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='modeladvice',
            name='RED_FLAG',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='modelsecrets',
            name='RED_FLAG',
            field=models.BooleanField(default=False),
        ),
    ]