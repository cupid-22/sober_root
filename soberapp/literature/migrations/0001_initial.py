# Generated by Django 4.1.2 on 2022-11-01 10:38

from django.db import migrations, models
import django.db.models.deletion
import literature.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Literature",
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
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=100)),
                (
                    "subtitle",
                    models.CharField(
                        help_text="Example: Edition of the literatures", max_length=50
                    ),
                ),
                ("is_subtitle_display_active", models.BooleanField(default=True)),
                ("is_sequence_display_active", models.BooleanField(default=True)),
            ],
            options={
                "db_table": "literature",
            },
        ),
        migrations.CreateModel(
            name="LiteratureSubSection",
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
                ("title", models.CharField(max_length=100)),
                ("subtitle", models.CharField(max_length=50)),
                ("main_content", models.TextField()),
                ("start_page", models.PositiveIntegerField()),
                (
                    "end_page",
                    models.PositiveIntegerField(),
                ),
                (
                    "literature",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="literature",
                        to="literature.literature",
                    ),
                ),
            ],
            options={
                "db_table": "literature_sub_section",
            },
        ),
    ]
