# Generated by Django 4.0.5 on 2022-10-14 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ksrtc', '0011_remove_passform_age_remove_passform_time_periode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='passform',
            name='age',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]