# Generated by Django 4.1.2 on 2023-03-02 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ksrtc', '0033_alter_passform_adhaar_image_alter_passform_idimage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passform',
            name='adhaar_image',
        ),
        migrations.RemoveField(
            model_name='passform',
            name='idimage',
        ),
        migrations.RemoveField(
            model_name='passform',
            name='profileimage',
        ),
    ]