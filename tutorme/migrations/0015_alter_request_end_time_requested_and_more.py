# Generated by Django 4.1.6 on 2023-04-12 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorme', '0014_remove_tutor_available_times_tutortimes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='end_time_requested',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='request',
            name='start_time_requested',
            field=models.CharField(default='', max_length=10),
        ),
    ]