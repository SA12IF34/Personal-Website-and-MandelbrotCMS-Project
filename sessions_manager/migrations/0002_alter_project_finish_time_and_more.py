# Generated by Django 4.2.7 on 2023-11-24 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sessions_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='finish_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='starting_time',
            field=models.DateField(blank=True, null=True),
        ),
    ]
