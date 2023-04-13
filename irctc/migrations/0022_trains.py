# Generated by Django 4.1.7 on 2023-04-13 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("irctc", "0021_trainpassform_amount_trainpassform_end_date_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Trains",
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
                ("train_no", models.IntegerField(blank=True, null=True)),
                (
                    "Route_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trains_route",
                        to="irctc.trainroute",
                    ),
                ),
            ],
        ),
    ]