# Generated by Django 4.1.2 on 2023-03-01 23:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ksrtc', '0031_alter_passform_profileimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='passform',
            name='dob',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
