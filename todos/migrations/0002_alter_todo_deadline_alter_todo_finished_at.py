# Generated by Django 5.2.4 on 2025-07-18 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='finished_at',
            field=models.DateField(null=True),
        ),
    ]
