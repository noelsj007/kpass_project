# Generated by Django 4.1.2 on 2023-03-27 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0011_dailybuspassview_pass_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="dailybuspassview",
            old_name="pass_id",
            new_name="pass_identity",
        ),
    ]