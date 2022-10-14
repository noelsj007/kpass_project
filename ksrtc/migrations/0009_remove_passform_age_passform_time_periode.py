# Generated by Django 4.0.5 on 2022-10-14 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ksrtc', '0008_remove_passform_time_periode_passform_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passform',
            name='age',
        ),
        migrations.AddField(
            model_name='passform',
            name='time_periode',
            field=models.CharField(blank=True, choices=[('onemonth', 'onemonth'), ('threemonths', 'threemonths'), ('sixmonths', 'sixmonths'), ('oneyear', 'oneyear')], max_length=50, null=True),
        ),
    ]