# Generated by Django 4.1.2 on 2023-03-25 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ksrtc", "0051_passform_payment_id_passform_signature"),
    ]

    operations = [
        migrations.AddField(
            model_name="passform",
            name="is_verified",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]