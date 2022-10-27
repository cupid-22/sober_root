# Generated by Django 4.1.2 on 2022-10-27 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="social_type",
            field=models.IntegerField(
                choices=[
                    (1, "Facebook Login"),
                    (2, "Google Login"),
                    (3, "Apple Login"),
                    (4, "Admin Login"),
                ]
            ),
        ),
    ]
