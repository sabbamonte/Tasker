# Generated by Django 3.1.3 on 2020-12-01 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasker', '0016_auto_20201201_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='links',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
