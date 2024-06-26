# Generated by Django 4.2.7 on 2024-01-12 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sessions_manager', '0004_remove_project_type'),
        ('learning_tracker', '0001_initial'),
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='learning_materials',
            field=models.ManyToManyField(blank=True, to='learning_tracker.material'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='projects',
            field=models.ManyToManyField(blank=True, to='sessions_manager.project'),
        ),
    ]
