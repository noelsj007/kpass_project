# Generated by Django 4.1.7 on 2023-04-05 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("irctc", "0020_trainstudentpassform_dob_trainstudentpassform_user"),
        ("users", "0012_rename_pass_id_dailybuspassview_pass_identity"),
    ]

    operations = [
        migrations.CreateModel(
            name="DailyTrainstPassView",
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
                ("end_date", models.DateField()),
                ("today", models.DateField()),
                ("checkbox1", models.BooleanField(default=False)),
                ("checkbox2", models.BooleanField(default=False)),
                (
                    "pass_identity",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="irctc.trainstudentpassform",
                    ),
                ),
            ],
        ),
    ]