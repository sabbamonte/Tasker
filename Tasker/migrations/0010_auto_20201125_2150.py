# Generated by Django 3.1.3 on 2020-11-25 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tasker', '0009_auto_20201125_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='links',
        ),
        migrations.AddField(
            model_name='url',
            name='subject',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Tasker.subject'),
        ),
    ]
