# Generated by Django 4.1.2 on 2022-11-11 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ksrtc", "0030_subtime_sub_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="passform",
            name="profileimage",
            field=models.ImageField(
                default=None,
                null=True,
                upload_to="users/static/ksrtcimage/profileimage",
            ),
        ),
    ]
