# Generated by Django 3.1.3 on 2020-11-25 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasker', '0010_auto_20201125_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='name',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
