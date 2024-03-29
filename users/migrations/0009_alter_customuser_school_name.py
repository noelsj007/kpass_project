# Generated by Django 4.1.2 on 2022-10-27 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("adminapp", "0009_schooldetail_school_place"),
        ("users", "0008_customuser_is_student_customuser_school_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="school_name",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="student_school",
                to="adminapp.schooldetail",
            ),
        ),
    ]
