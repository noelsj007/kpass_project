# Generated by Django 4.1.2 on 2022-11-11 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ksrtc", "0027_subtime_sub_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="passform",
            name="adhaar_image",
            field=models.ImageField(
                default=None, null=True, upload_to="users/static/ksrtcimage/adhaar"
            ),
        ),
        migrations.AlterField(
            model_name="passform",
            name="idimage",
            field=models.ImageField(
                default=None, null=True, upload_to="users/static/ksrtcimage/idimage"
            ),
        ),
        migrations.AlterField(
            model_name="passform",
            name="profileimage",
            field=models.ImageField(
                default=None,
                null=True,
                upload_to="users/static/kstrcimage/profileimage",
            ),
        ),
    ]