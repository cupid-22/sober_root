# Generated by Django 4.1.2 on 2022-11-29 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("literature", "0002_remove_literaturesubsection_end_page_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="literature",
            name="is_subtitle_active",
            field=models.BooleanField(
                help_text="To keep subtitle visible on app screen"
            ),
        ),
    ]