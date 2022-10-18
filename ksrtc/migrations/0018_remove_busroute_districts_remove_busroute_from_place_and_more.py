# Generated by Django 4.0.5 on 2022-10-14 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ksrtc', '0017_places'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='busroute',
            name='districts',
        ),
        migrations.RemoveField(
            model_name='busroute',
            name='from_place',
        ),
        migrations.RemoveField(
            model_name='busroute',
            name='states',
        ),
        migrations.RemoveField(
            model_name='busroute',
            name='to_place',
        ),
        migrations.AddField(
            model_name='busroute',
            name='start_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ksrtc.places'),
        ),
    ]