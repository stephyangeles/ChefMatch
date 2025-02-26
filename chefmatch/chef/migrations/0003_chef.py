# Generated by Django 5.1.6 on 2025-02-26 16:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("chef", "0002_delete_chef")]

    operations = [
        migrations.CreateModel(
            name="Chef",
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
                ("name", models.CharField(max_length=255)),
                ("bio", models.TextField()),
                (
                    "reservation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="chef.reservation",
                    ),
                ),
                (
                    "specialty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="chef.specialty"
                    ),
                ),
            ],
        )
    ]
