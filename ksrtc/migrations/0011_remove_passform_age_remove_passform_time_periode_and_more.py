# Generated by Django 4.0.5 on 2022-10-14 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ksrtc', '0010_passform_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passform',
            name='age',
        ),
        migrations.RemoveField(
            model_name='passform',
            name='time_periode',
        ),
        migrations.AddField(
            model_name='passform',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
