# Generated by Django 4.0.5 on 2022-10-08 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irctc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainroutes',
            name='from_place',
        ),
        migrations.RemoveField(
            model_name='trainroutes',
            name='to_place',
        ),
    ]
