# Generated by Django 4.1.6 on 2023-03-16 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorme', '0004_request_created_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_timestamp_rating', models.DateTimeField(auto_now_add=True)),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, 'Poor'), (2, 'Fair'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=3)),
                ('student_who_rated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_who_rated', to='tutorme.appuser')),
                ('tutor_who_was_rated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor_who_was_rated', to='tutorme.appuser')),
            ],
        ),
    ]
