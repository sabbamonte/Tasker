# Generated by Django 3.1.3 on 2020-11-28 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasker', '0012_auto_20201128_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='category',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
