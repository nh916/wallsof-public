# Generated by Django 2.2.1 on 2019-07-02 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallOf', '0031_modelcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelcomment',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='modelcomment',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]