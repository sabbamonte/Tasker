# Generated by Django 3.1.3 on 2020-11-25 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tasker', '0005_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='subject',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='all_links', to='Tasker.subject'),
        ),
    ]
