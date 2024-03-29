# Generated by Django 4.0.5 on 2022-10-18 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0009_schooldetail_school_place'),
        ('users', '0008_customuser_is_student_customuser_school_name_and_more'),
        ('irctc', '0009_delete_schooldetail_remove_subtime_sub_price_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PassForm',
            new_name='TrainPassForm',
        ),
        migrations.RenameModel(
            old_name='Place',
            new_name='TrainPlace',
        ),
        migrations.RenameModel(
            old_name='StudentPassForm',
            new_name='TrainStudentPassForm',
        ),
        migrations.RenameModel(
            old_name='SubTime',
            new_name='TrainSubTime',
        ),
    ]
