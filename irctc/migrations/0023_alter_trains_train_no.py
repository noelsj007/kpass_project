# Generated by Django 4.1.7 on 2023-04-13 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("irctc", "0022_trains"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trains",
            name="train_no",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
