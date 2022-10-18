# Generated by Django 4.0.5 on 2022-10-16 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0008_schooldetail'),
        ('irctc', '0008_studentpassform'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SchoolDetail',
        ),
        migrations.RemoveField(
            model_name='subtime',
            name='sub_price',
        ),
        migrations.AddField(
            model_name='passform',
            name='adhaar_image',
            field=models.ImageField(default=None, null=True, upload_to='static/irctcimage/adhaar'),
        ),
        migrations.AddField(
            model_name='passform',
            name='adhaar_no',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='passform',
            name='end_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pass_end_tp', to='irctc.place'),
        ),
        migrations.AddField(
            model_name='passform',
            name='mobile',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='passform',
            name='name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='passform',
            name='profileimage',
            field=models.ImageField(default=None, null=True, upload_to='static/irctcimage/profileimage'),
        ),
        migrations.AddField(
            model_name='passform',
            name='start_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pass_start_tp', to='irctc.place'),
        ),
        migrations.AddField(
            model_name='studentpassform',
            name='adhaar_image',
            field=models.ImageField(default=None, null=True, upload_to='static/irctcimage/adhaar'),
        ),
        migrations.AddField(
            model_name='studentpassform',
            name='adhaar_no',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='studentpassform',
            name='end_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pass_end_sp', to='irctc.place'),
        ),
        migrations.AddField(
            model_name='studentpassform',
            name='idimage',
            field=models.ImageField(default=None, null=True, upload_to='static/irctcimage/idimage'),
        ),
        migrations.AddField(
            model_name='studentpassform',
            name='mobile',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='studentpassform',
            name='name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='studentpassform',
            name='profileimage',
            field=models.ImageField(default=None, null=True, upload_to='static/irctcimage/profileimage'),
        ),
        migrations.AddField(
            model_name='studentpassform',
            name='school_name',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.schooldetail'),
        ),
        migrations.AddField(
            model_name='studentpassform',
            name='start_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pass_start_sp', to='irctc.place'),
        ),
        migrations.AlterField(
            model_name='passform',
            name='address',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='passform',
            name='age',
            field=models.IntegerField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='passform',
            name='time_periode',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='irctc.subtime'),
        ),
        migrations.AlterField(
            model_name='studentpassform',
            name='address',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentpassform',
            name='age',
            field=models.IntegerField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentpassform',
            name='time_periode',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='irctc.subtime'),
        ),
    ]