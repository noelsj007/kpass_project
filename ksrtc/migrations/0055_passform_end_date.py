# Generated by Django 4.1.2 on 2023-03-25 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ksrtc", "0054_alter_passform_verification_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="passform",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]