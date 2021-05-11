# Generated by Django 2.2 on 2021-05-11 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0002_auto_20210511_0729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myprofilemodel',
            name='email',
        ),
        migrations.RemoveField(
            model_name='myprofilemodel',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='myprofilemodel',
            name='last_name',
        ),
        migrations.AddField(
            model_name='myprofilemodel',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='thumbpath'),
        ),
    ]
