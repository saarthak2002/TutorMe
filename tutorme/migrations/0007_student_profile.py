# Generated by Django 4.1.6 on 2023-03-29 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorme', '0006_ratings_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[(1, 'First Year'), (2, 'Second Year'), (3, 'Third Year'), (4, 'Fourth Year'), (5, 'Graduate')], max_length=12)),
                ('help_description', models.TextField()),
                ('bio', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorme.appuser')),
            ],
        ),
    ]