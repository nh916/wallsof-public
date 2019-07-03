# Generated by Django 2.2.1 on 2019-07-02 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('wallOf', '0030_auto_20190627_0150'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=120)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('only_date', models.DateField(auto_now_add=True)),
                ('up_vote', models.IntegerField(blank=True, default=0)),
                ('down_vote', models.IntegerField(blank=True, default=0)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
    ]
