# Generated by Django 4.1.6 on 2023-04-21 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tutorme", "0017_alter_appuser_help_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="Chat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "student_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="student_in_chat",
                        to="tutorme.appuser",
                    ),
                ),
                (
                    "tutor_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tutor_in_chat",
                        to="tutorme.appuser",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_timestamp_message", models.DateTimeField(auto_now_add=True)),
                ("message", models.CharField(max_length=500)),
                (
                    "chat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tutorme.chat"
                    ),
                ),
                (
                    "from_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_who_sent_message",
                        to="tutorme.appuser",
                    ),
                ),
                (
                    "to_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_who_received_message",
                        to="tutorme.appuser",
                    ),
                ),
            ],
        ),
    ]
