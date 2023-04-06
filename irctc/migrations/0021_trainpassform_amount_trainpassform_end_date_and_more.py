# Generated by Django 4.1.7 on 2023-04-05 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("irctc", "0020_trainstudentpassform_dob_trainstudentpassform_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="trainpassform",
            name="amount",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="trainpassform",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="trainpassform",
            name="order_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="trainpassform",
            name="paid",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="trainpassform",
            name="payment_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="trainpassform",
            name="signature",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="trainpassform",
            name="trainst_rate",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="trainpassform",
            name="verification_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]